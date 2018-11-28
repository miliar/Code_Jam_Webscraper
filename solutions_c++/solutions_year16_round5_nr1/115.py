#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        string s;
        cin >> s;
        stack<char> S;
        int ans = 0;
        iter(it,s) {
            if (!S.empty() && S.top() == *it) {
                ans += 10;
                S.pop();
            } else {
                S.push(*it);
            }
        }
        int cnt = 0;
        while (!S.empty()) {
            cnt++;
            S.pop();
        }
        assert(cnt % 2 == 0);
        ans += cnt / 2 * 5;
        printf("Case #%d: %d\n", t + 1, ans);
    }
    return 0;
}

