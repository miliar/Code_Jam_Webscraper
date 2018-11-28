/**
 * Author : Parachvte (ryannx6@gmail.com)
 * Date   : 04/10/2016
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define range(i, a, b) for (int i = (a), _end_ = (b); i <= _end_; ++i)
#define rep(i, n) for (int i = (0), _end_ = (n); i < _end_; ++i)
#define pb push_back
#define mp make_pair
#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

char s[200];
int n;

char op(char c) {
    if (c == '+')
        return '-';
    else
        return '+';
}

void flip(char *s, int last) {
    for (int i = 0; i <= last / 2; i++) {
        int j = last - i;
        if (i == j) {
            s[i] = op(s[i]);
        } else {
            char si = s[i];
            s[i] = op(s[j]);
            s[j] = op(si);
        }
    }
}

int solve() {
    scanf("%s", s);
    n = (int)strlen(s);

    int steps = 0;
    while (true) {
        int last = n - 1;
        while (last >= 0 && s[last] == '+') last--;
        if (last == -1) break;

        if (s[0] == '+') {
            int i = 0;
            while (s[i] == '+') i++;
            flip(s, i - 1);
            steps++;
        }
        flip(s, last);
        steps++;
    }

    return steps;
}

int main() {
#ifdef DEBUG
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
#endif
    std::ios_base::sync_with_stdio(false);

    int T;
    scanf("%d", &T);
    rep(i, T) {
        printf("Case #%d: %d\n", i + 1, solve());
    }

    return 0;
}
