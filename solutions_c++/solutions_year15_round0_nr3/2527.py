#include <iostream>
#include <unordered_set>
#include <cmath>

using namespace std;

#define I 2
#define J 3
#define K 4
#define ONE 1

int mTable[4][4] = {
    {ONE, I, J, K},
    {I, -ONE, K, -J},
    {J, -K, -ONE, I},
    {K, J, -I, -ONE},
};

int charToCINT(char c) {
    switch (c) {
        case 'i':
            return I;
        case 'j':
            return J;
        case 'k':
            return K;
        case '1':
            return ONE;
        default:
            return (int) c;
    }
}

inline int compute_sign(int num) {
    return num >= 0? 1 : -1;
}

bool solve(string& s, int L, int X) {
    unordered_set<int> kPositions;
    int currCINT = ONE;
    int charIdx;
    int sign, cInt;
    for (int kIdx = L*X - 1; kIdx >= 2; --kIdx) {
        charIdx = kIdx % L;
        cInt = charToCINT(s[charIdx]);
        sign = compute_sign(currCINT);

        currCINT = sign * mTable[cInt - 1][abs(currCINT) - 1];
        if (currCINT == K) {
            kPositions.insert(kIdx);
        }
    }

    currCINT = ONE;
    for (int iIdx = 0; iIdx < L*X - 2; ++iIdx) {
        charIdx = iIdx % L;
        cInt = charToCINT(s[charIdx]);
        sign = compute_sign(currCINT);

        currCINT = sign * mTable[abs(currCINT) - 1][cInt - 1];
        if (currCINT != I) {
            continue;
        }

        int currCINTforJ = ONE;
        for (int jIdx = iIdx + 1; jIdx < L*X - 1; ++jIdx) {
            charIdx = jIdx % L;
            cInt = charToCINT(s[charIdx]);
            sign = compute_sign(currCINTforJ);

            currCINTforJ = sign * mTable[abs(currCINTforJ) - 1][cInt - 1];
            if (currCINTforJ != J) {
                continue;
            }

            int kIdx = jIdx + 1;
            if (kPositions.find(kIdx) != kPositions.end()) {
                return true;
            }
        }
    }

    return false;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int L, X;
        cin >> L >> X;
        string s;
        cin >> s;
        bool equiv = solve(s, L, X);
        if (equiv) {
            cout << "Case #" << i + 1 << ": YES\n";
        } else {
            cout << "Case #" << i + 1 << ": NO\n";
        }
    }

    return 0;
}
