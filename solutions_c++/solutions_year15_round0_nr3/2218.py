#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e4 + 10;

const int TRANS[4][4] = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0},
};

const int NEGA[4][4] = {
    {0, 0, 0, 0},
    {0, 1, 0, 1},
    {0, 1, 1, 0},
    {0, 0, 1, 1},
};

int trans[4][4], nega[4][4];

int leftNum[MAXN], leftNega[MAXN];

inline void print(int num, int nega) {
    if (nega) {
        putchar('-');
    }
    if (num == 0) {
        putchar('1');
    } else {
        putchar('i' + num - 1);
    }
}

int main() {
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);
    int T, l, x;
    string tmp;
    scanf("%d", &T);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                if (TRANS[i][k] == j) {
                    trans[i][j] = k;
                    nega[i][j] = NEGA[i][k];
                }
            }
        }
    }
    for (int t = 1; t <= T; ++t) {
        cin >> l >> x;
        cin >> tmp;
        string s;
        while (x--) {
            s += tmp;
        }
        //cout << tmp << endl;
        int lastNum = 0;
        int lastNega = 0;
        for (int i = 0; i < s.length(); ++i) {
            leftNega[i] = lastNega ^ NEGA[lastNum][s[i] - 'i' + 1];
            leftNum[i] = TRANS[lastNum][s[i] - 'i' + 1];
            lastNum = leftNum[i];
            lastNega = leftNega[i];
            //print(lastNum, lastNega);
            //cout << ' ';
        }
        //cout << endl;
        bool found = false;
        for (int i = 0; i < s.length() && !found; ++i) {
            if (leftNum[i] != 1 || leftNega[i] != 0) {
                continue;
            }
            for (int j = i + 2; j < s.length(); ++j) {
                int midNega = leftNega[i] ^ leftNega[j - 1] ^ nega[leftNum[i]][leftNum[j - 1]];
                int midNum = trans[leftNum[i]][leftNum[j - 1]];
                if (midNum != 2 || midNega != 0) {
                    continue;
                }
                int rightNega = leftNega[j - 1] ^ leftNega[s.length() - 1] ^ nega[leftNum[j - 1]][leftNum[s.length() - 1]];
                int rightNum = trans[leftNum[j - 1]][leftNum[s.length() - 1]];
                if (rightNum == 3 && rightNega == 0) {
                    //cout << i << " " << j << endl;
                    found = true;
                    break;
                }
            }
        }
        printf("Case #%d: %s\n", t, found ? "YES" : "NO");
    }
    return 0;
}
