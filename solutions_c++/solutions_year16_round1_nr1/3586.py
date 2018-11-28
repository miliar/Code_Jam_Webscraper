/*
 * Created by KeigoOgawa
 */

#include <cstdio>
#include <iostream>

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
typedef pair<int, int> P;

const int MAX_S = 1000;

int T;
string S;

string solve() {
    string ans = "";
    ans += S[0];
    FOR(i, 1, S.size()) {
        if (S[i] < ans[0]) {
            ans += S[i];
        } else {
            string tmp = "";
            tmp += S[i] + ans;
            ans = tmp;
        }
    }
    return ans;
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> T;

    REP(i, T) {
        cin >> S;
        printf("Case #%d: %s\n", i + 1, solve().c_str());
    }

    return 0;
}
