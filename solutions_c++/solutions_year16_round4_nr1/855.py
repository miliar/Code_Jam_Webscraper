#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;


char ans[20][5000];

string res;

bool possible(int lvl, int cnt, int R, int P, int S) {
    if (R < 0 || P < 0 || S < 0)
        return false;
    if (P + R + S == 1) {
        if (P == 1)
            res = "P";
        if (R == 1)
            res = "R";
        if (S == 1)
            res = "S";
        return true;
    }
    if ((R + S - P) % 2 != 0)
        return false;
    int b = (R + S - P) / 2;
    int c = S - b;
    int a = P - c;
    return possible(lvl + 1, cnt/2, b, a, c);
}

string build(char c, int N) {
    if (N == 0) {
        string res;
        res.push_back(c);
        return res;
    };
    char b;
    if (c == 'P') {
        b = 'R';
    }
    if (c == 'R') {
        b = 'S';
    }
    if (c == 'S') {
        b = 'P';
    }
    string s1 = build(c, N - 1);
    string s2 = build(b, N - 1);
    if (s1 < s2)
        return s1 + s2;
    return s2 + s1;
}

void solve() {
    int N;
    int R, P, S;
    scanf("%d%d%d%d", &N, &R, &P, &S);
    if (!possible(0, 0, R, P, S)) {
        puts("IMPOSSIBLE");
        return;
    }
    puts(build(res[0], N).c_str());
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}