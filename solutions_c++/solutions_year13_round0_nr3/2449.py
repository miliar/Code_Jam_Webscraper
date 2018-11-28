#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

long long L, R;

ifstream fin1("precalc.txt");
ifstream fin2("input.txt");
ofstream fout("output.txt");

void readData() {
    fin2 >> L >> R;
}

set<long long> square;

bool isBetween(long long x, long long l, long long r) {
    return (x >= l) && (x <= r);
}

int solve() {
    int answer = 0;
    for (set<long long>::iterator it = square.begin(); it != square.end(); ++it) {
        if (isBetween((*it) * (*it), L, R)) {
            answer ++;
        }
    }
    return answer;
}

void init() {
    long long t;
    while (fin1 >> t) {
        square.insert(t);
    }
}

int main() {
    int answer = 0;
    init();
    int T;
    fin2 >> T;
    for (int i = 0; i < T; ++i) {
        readData();
        answer = solve();
        fout << "Case #" << i + 1 << ": " << answer << endl;
    }
    return 0;
}
