enum Contest { CodeChef, CodeJam };
enum IOBinding { File, StandartStream };

Contest contest = CodeJam;

IOBinding inputBinding = File;
//IOBinding inputBinding = StandartStream;

IOBinding outputBinding = File;
//IOBinding outputBinding = StandartStream;

#include <string>
#include <fstream>
#include <istream>
#include <ostream>
#include <iostream>

std::istream *input;
std::ostream *output;

#include <algorithm>
#include <vector>

typedef std::vector <int> IVec;

class Problem {
public:
    Problem();
    ~Problem();
    void solve();

private:
    int numSpecial(int max);
    int N, *vec_;
};

Problem::Problem() {
    *input >> N;
    vec_ = new int [N];
    for(int n = 0; n < N; ++n)
        *input >> vec_[n];
}

Problem::~Problem() {
    delete[] vec_;
}

void Problem::solve() {
    int min = 1, max = 0;
    for(int n = 0; n < N; ++n)
        if (vec_[n] > max) max = vec_[n];

    int bestTime = max;

    int working = true;
    while(working) {
        working = false;
        int minmin = min;
        int mid = (min + max) / 2;
        int nSpec = numSpecial(mid);
        int time = mid + nSpec;
        if (time < bestTime) {
            if (time < max) working = true;
            max = bestTime = time;
        }
        else min = mid - nSpec;
        if (min < 1) min = 1;
        if (min != minmin) working = true;
    }

    for(int i = min; i < max; ++i) {
        int time = i + numSpecial(i);
        if (time < bestTime) bestTime = time;
    }

    *output << bestTime << '\n';
}

int Problem::numSpecial(int max) {
    int res = 0;
    for(int n = 0; n < N; ++n) {
        if (!(vec_[n] % max)) --res;
        res += vec_[n] / max;
    }
    return res;
}

void solveCase() {
    Problem p;
    p.solve();
}

int main(int argc, char *argv[])
{
    std::ios_base::sync_with_stdio(false);

    if (inputBinding == File)
        input = new std::ifstream("input.txt");
    else input = &std::cin;

    if (outputBinding == File)
        output = new std::ofstream("output.txt");
    else output = &std::cout;

    int T; *input >> T;
    for(int t = 1; t <= T; ++t) {
        if (contest == CodeJam)
            *output << "Case #" << t << ": ";
        solveCase();
    }

    if (inputBinding == File) delete input;
    if (outputBinding == File) delete output;

    return 0;
}
