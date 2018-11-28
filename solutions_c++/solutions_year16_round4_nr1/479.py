#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int N;
int a[10], s[10], t[10];
int c[10101], cc[10101];
vector<int> ans;

bool check(int finalwin) {
    s[0] = s[1] = s[2] = 0;
    s[finalwin] = 1;

    for (int i = 1; i <= N; ++i) {
        t[0] = s[0] + s[2];
        t[1] = s[0] + s[1];
        t[2] = s[1] + s[2];

        s[0] = t[0];
        s[1] = t[1];
        s[2] = t[2];
    }

    if (s[0] == a[0] && s[1] == a[1] && s[2] == a[2]) {
        return true;
    }
    return false;
}

/*
bool smaller(int l, int r, int h) {
    for (int i = 0; i < h; ++i) {
        if (cc[r + i] < cc[l + i]) {
            return  true;
        }
    }
    return false;
}*/

bool smaller(vector<int> L, vector<int> R) {
    for (int i = 0, len = L.size(); i < len; ++i) {
        if (R.at(i) < L.at(i)) {
            return true;
        }
    }
    return false;
}

vector<int> hit(int level, int who) {
    int p1, p2;

    if (who == 0) {
        p1 = 0;
        p2 = 1;
    }
    if (who == 1) {
        p1 = 1;
        p2 = 2;
    }
    if (who == 2) {
        p1 = 0;
        p2 = 2;
    }

    if (level == N) {
        vector<int> vi;
        vi.clear();
        vi.push_back(p1);
        vi.push_back(p2);
        return vi;
    }

    vector<int> L;
    vector<int> R;

    L = hit(level + 1, p1);
    R = hit(level + 1, p2);

    if (smaller(L, R)) {
        vector<int> T;
        T = L;
        L = R;
        R = T;
    }

    for (int len = R.size(), i = 0; i < len; ++i) {
        L.push_back(R.at(i));
    }

    return L;
}

/*
void genChar(int finalwin) {
    c[1] = finalwin;

    for (int i = 1; i <= N; ++i) {
        int tLen = 1 << i;
        int halfLen = 1 << (i - 1);
        for (int j = 1; j <= halfLen; ++j) {
            if (c[j] == 0) {
                cc[j + j - 1] = 0;
                cc[j + j] = 1;
            };
            if (c[j] == 1) {
                cc[j + j - 1] = 1;
                cc[j + j] = 2;
            }
            if (c[j] == 2) {
                cc[j + j - 1] = 0;
                cc[j + j] = 2;
            }
        }
        for (int i = 1; i <=
        if (smaller(1, 1 + halfLen, halfLen)) {
            for (int j = 1; j <= halfLen; ++j) {
                swap(cc[j], cc[j + halfLen]);
            }
        }
        for (int j = 1; j <= (1 << i); ++j) {
            c[j] = cc[j];
        }
    }
}
*/

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int Cas = 1; Cas <= T; ++Cas) {

        bool noSolution = true;

        scanf("%d %d %d %d", &N, &a[1], &a[0], &a[2]); // R, P, S
        for (int i = 0; i < 3; ++i) {
            if (check(i)) {
                noSolution = false;
                ans = hit(1, i);
                break;
            }
        }

        printf("Case #%d: ", Cas);

        if (noSolution) {
            printf("%s\n", "IMPOSSIBLE");
        } else {
            for (int i = 0, len = ans.size(); i < len; ++i) {
                if (ans.at(i) == 0) {
                    printf("%c", 'P');
                }
                if (ans.at(i) == 1) {
                    printf("%c", 'R');
                }
                if (ans.at(i) == 2) {
                    printf("%c", 'S');
                }
            }
            puts("");
        }
    }
    return 0;
}
