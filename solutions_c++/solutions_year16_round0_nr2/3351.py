#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define RREP(i,s,e) for (i = s; i >= e; i--)
#define rrep(i,n) RREP(i,n,0)
#define REP(i,s,e) for (i = s; i < e; i++)
#define rep(i,n) REP(i,0,n)
#define INF 100000000

typedef long long ll;

int main() {
    int i, t;
    cin >> t;
    rep (i,t) {
        string s;
        cin >> s;
        char now = s.front();
        int ans = s.back() == '+' ? 0 : 1;
        for (char c : s) {
            if (c != now) {
                ans++;
                now = c;
            }
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}

