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

string problem = "/Users/apierce/codejam16/codejam/Round2/B-large";
FILE *infile;
FILE *outfile;

typedef long long lld;

lld next_lld() {
    lld result = 0;
    fscanf(infile, "%lld", &result);
    return result;
}

double next_double() {
    double result = 0;
    fscanf(infile, "%lf", &result);
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

double get_tie_probability(vector<double> vals) {
    vector<double> probabilities;
    probabilities.push_back(1.0);
    for (double newVal : vals) {
        vector<double> new_probabilities(probabilities.size() + 1, 0);
        for (int i = 0; i < probabilities.size(); i++) {
            new_probabilities[i] += probabilities[i] * (1 - newVal);
            new_probabilities[i + 1] += probabilities[i] * newVal;
        }
        probabilities.swap(new_probabilities);
    }
    return probabilities[probabilities.size() / 2];
}

string handle_case() {
    lld n = next_lld();
    lld k = next_lld();
    vector<double> vals;
    for (int i = 0; i < n; i++) {
        vals.push_back(next_double());
    }
    sort(vals.begin(), vals.end());

    double best_probability = 0.0;
    for (int num_from_start = 0; num_from_start <= k; num_from_start++) {
        vector<double> result;
        for (int i = 0; i < num_from_start; i++) {
            result.push_back(vals[i]);
        }
        for (int i = 0; i < (k - num_from_start); i++) {
            result.push_back(vals[n - i - 1]);
        }
        best_probability = max(best_probability, get_tie_probability(result));
    }

    char buf[1000];
    sprintf(buf, "%.012lf", best_probability);
    stringstream ss;
    ss << buf;
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