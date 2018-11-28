/*
 * Created by KeigoOgawa on 4/9/16.
 */


#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <cmath>

#define INF (int)1e8
#define EPS 1e-10
#define FOR(i, a, b) for (int i=(a);i<(b);i++)
#define RFOR(i, a, b) for (int i=(b)-1;i>=(a);i--)
#define REP(i, n) for (int i=0;i<(n);i++)
#define RREP(i, n) for (int i=(n)-1;i>=0;i--)
#define MIN(a, b) (a>b?b:a)
#define MAX(a, b) (a>b?a:b)
#define debug(x) cout<<#x<<": "<<x<<endl
#define all(a) (a).begin(),(a).end()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;

const int MAX_S = 100;

int T;
string S;

int solve() {
    string s;
    s += S[0];
    for (int i = 1; i < S.size(); ++i) {
        if (S[i - 1] != S[i]) {
            s += S[i];
        }
    }

    if (s.length() % 2 == 1) {
        if (s[0] == '+') {
            return (int) s.size() - 1;
        } else {
            return (int) s.size();
        }
    } else {
        if (s[0] == '-') {
            return (int) s.size() - 1;
        } else {
            return (int) s.size();
        }
    }
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> S;
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
