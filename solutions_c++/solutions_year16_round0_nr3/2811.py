#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

#define RREP(i,s,e) for (i = s; i >= e; i--)
#define rrep(i,n) RREP(i,n,0)
#define REP(i,s,e) for (i = s; i < e; i++)
#define rep(i,n) REP(i,0,n)
#define INF 100000000

typedef long long ll;

ll divisor(ll x) {
    ll i;
    REP (i,2,sqrt(x)) {
        if (x % i == 0)
            return i;
    }
    return 1;
}

int main() {
    int i, t;
    cin >> t;
    rep (i,t) {
        int n, j, k, base;
        int ans[9];
        cin >> n >> j;
        cout << "Case #" << i+1 << ":" << endl;
        for (int x = (1<<n-1)+1; j > 0 && x < 1<<n; x+=2) {
            bool found = true;
            int d = divisor(x);
            if (d == 1)
                found = false;
            else
                ans[0] = d;
            REP (base,3,11) {
                ll num = 0;
                ll b = 1;
                int tmp = x;
                while (tmp > 0) {
                    num += tmp % 2 ? b : 0;
                    b *= base;
                    tmp /= 2;
                }
                d = divisor(num);
                if (d == 1)
                    found = false;
                else
                    ans[base-2] = d;
            }
            if (!found)
                continue;
            int tmp = x;
            string s;
            while (tmp > 0) {
                s.push_back(tmp%2?'1':'0');
                tmp /= 2;
            }
            reverse(s.begin(),s.end());
            cout << s << " ";
            rep (k,9) cout << ans[k] << " ";
            cout << endl;
            j--;
        }
    }
    return 0;
}

