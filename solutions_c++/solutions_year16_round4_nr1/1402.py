#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <utility>
#include <numeric>
#include <string.h>

using namespace std;

typedef unsigned long long ulong;
typedef unsigned int uint;
typedef long long int64;


inline ulong max(ulong a, ulong b) {
    return a > b ? a : b;
}

inline ulong min(ulong a, ulong b) {
    return a < b ? a : b;
}

bool finished = false;
ulong N = 0;
ulong powN = 0;
string lineupStr;

string adjust(string lineup) {
    string lineup1 = lineup;
    for (ulong len = 1; len * 2 <= powN; len *= 2) {
        string adjusted;
        adjusted.reserve(lineup.size());
        //cout << "check len " << len << endl;
        for (ulong idx = 0; idx < powN; idx += 2 * len) {
            string s1 = lineup.substr(idx, len);
            string s2 = lineup.substr(idx + len, len);
            //cout << "idx " << idx << " s1 = " << s1 <<", s2 = " << s2 << endl;
            if (s1 < s2) {
                adjusted += s1;
                adjusted += s2;
            } else {
                adjusted += s2;
                adjusted += s1;
            }
        }
        lineup = adjusted;
    }
    //cout << "adjusted " << lineup1 << " to " << lineup <<  ", powN = " << powN << endl;
    return lineup;
}

string grow(char start) {
    string lineup;
    lineup.push_back(start);

    string res;

    for (int i = 0; i < N; ++i) {
        for (char c : lineup) {
            if (c == 'P') {
                res.push_back('P');
                res.push_back('R');
            } else if (c == 'R') {
                res.push_back('R');
                res.push_back('S');
            } else { //(c == 'S') {
                res.push_back('P');
                res.push_back('S');
            }
        }

        lineup = std::move(res);
        res.clear();
    }
    return adjust(lineup);
}

bool verify(const string& lineup, ulong R, ulong P, ulong S) {
    return 
        std::count(lineup.begin(), lineup.end(), 'R') == R
        && std::count(lineup.begin(), lineup.end(), 'P') == P
        && std::count(lineup.begin(), lineup.end(), 'S') == S;

}

int main() {
    ulong numTests = 0;
    cin >> numTests;
    for (ulong t = 1; t <= numTests; ++t) {
        ulong P, R, S;
        cin >> N >> R >> P >> S;
        powN = 1 << N;

        auto l1 = grow('P');
        auto l2 = grow('R');
        auto l3 = grow('S');

        //cout << l1 << endl << l2 << endl << l3 << endl;
        vector<string> variants;
        if (verify(l1, R, P, S))
            variants.push_back(l1);
        if (verify(l2, R, P, S))
            variants.push_back(l2);
        if (verify(l3, R, P, S))
            variants.push_back(l3);
        string res = variants.empty() ? "IMPOSSIBLE" : variants.front();

        //cout << l1s << ' ' << l2s << ' ' << l3s << endl;

        cout << "Case #" << t << ": "  << res << endl;
    }
    return 0;
}

