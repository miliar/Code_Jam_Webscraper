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

bool num[10];

int main() {
    int i, t;
    cin >> t;
    rep (i,t) {
        int n, ans;
        int mask = 0;
        cin >> n;
        cout << "Case #" << i+1 << ": ";
        if (n == 0)
            cout << "INSOMNIA" << endl;
        else {
            for (ans = n; mask != 0x3ff; ans+=n) {
                int x = ans;
                while (x > 0) {
                    mask |= 1 << (x % 10);
                    x /= 10;
                }
            }
            cout << ans-n << endl;
        }
    }
    return 0;
}

