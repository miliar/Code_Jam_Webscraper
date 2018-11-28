#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <unistd.h>
#include <unordered_set>
#include <sstream>
#include <set>
#include <map>

using namespace std;

string problem = "/Users/apierce/codejam16/codejam/Round2/A-large";
FILE *infile;
FILE *outfile;

typedef long long lld;

lld next_lld() {
    lld result = 0;
    fscanf(infile, "%lld", &result);
    return result;
}

string next_string() {
    char result[1000];
    fscanf(infile, "%s", result);
    return string(result);
}

int next_int() {
    int result = 0;
    fscanf(infile, "%d", &result);
    return result;
}

vector<int> next_int_vector(int n) {
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        result[i] = next_int();
    }
    return result;
}


map<pair<int, char>, string> memo;

string best_solution(lld num_rounds, char winner) {
    if (num_rounds == 0) {
        string s;
        s.push_back(winner);
        return s;
    }

    auto key = make_pair(num_rounds, winner);
    if (!memo.count(key)) {
        string subtree1;
        string subtree2;
        if (winner == 'R') {
            subtree1 = best_solution(num_rounds - 1, 'R');
            subtree2 = best_solution(num_rounds - 1, 'S');
        } else if (winner == 'P') {
            subtree1 = best_solution(num_rounds - 1, 'P');
            subtree2 = best_solution(num_rounds - 1, 'R');
        } else if (winner == 'S') {
            subtree1 = best_solution(num_rounds - 1, 'S');
            subtree2 = best_solution(num_rounds - 1, 'P');
        }
        memo[key] = min(subtree1 + subtree2, subtree2 + subtree1);
    }
    return memo[key];
}

string handle_case() {
    lld n = next_lld();
    lld numRock = next_lld();
    lld numPaper = next_lld();
    lld numScissors = next_lld();

    string best1 = best_solution(n, 'R');
    string best2 = best_solution(n, 'P');
    string best3 = best_solution(n, 'S');

    vector<string> possible_solutions;
    possible_solutions.push_back(best_solution(n, 'R'));
    possible_solutions.push_back(best_solution(n, 'P'));
    possible_solutions.push_back(best_solution(n, 'S'));

    vector<string> solutions;
    for (string sol : possible_solutions) {
        lld countedRock = 0;
        lld countedPaper = 0;
        lld countedScissors = 0;
        for (char c : sol) {
            if (c == 'R') {
                countedRock++;
            }
            if (c == 'P') {
                countedPaper++;
            }
            if (c == 'S') {
                countedScissors++;
            }
        }
        if (countedRock == numRock && countedPaper == numPaper && countedScissors == numScissors) {
            solutions.push_back(sol);
        }
    }
    sort(solutions.begin(), solutions.end());

    stringstream ss;
    if (solutions.size()) {
        ss << solutions[0];
    } else {
        ss << "IMPOSSIBLE";
    }
    return ss.str();
}

int main() {
    string infilename = problem + ".in";
    string outfilename = problem + ".out";
    infile = fopen(infilename.c_str(), "r");
    if (infile == nullptr) {
        printf("File %s not found!", infilename.c_str());
        return 1;
    }
    outfile = fopen(outfilename.c_str(), "w");

    lld n_cases = next_lld();
    for (lld case_num = 1; case_num <= n_cases; ++case_num) {
        string result = handle_case();
        printf("Case #%lld: %s\n", case_num, result.c_str());
        fprintf(outfile, "Case #%lld: %s\n", case_num, result.c_str());
    }
    return 0;
}