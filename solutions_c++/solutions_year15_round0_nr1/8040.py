#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

ifstream fin("standingovation.in");
ofstream fout("standingovation.out");

int solve(int sMax, string s) {
    int res = 0;

    int soFar = s[0] - '0';
    for (int i = 1; i <= sMax; i += 1) {
        if (soFar < i) {
            int add = i - soFar;
            res += add;
            soFar += add;
        }
        soFar += s[i] - '0';
    }
    return res;
}

int main() {
    int T;
    fin >> T;

    for (int t = 1; t <= T; t += 1) {
        int sMax;
        string s;
        fin >> sMax >> s;
        fout << "Case #" << t << ": " << solve(sMax, s) << '\n';
    }
    return 0;
}