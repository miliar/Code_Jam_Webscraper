#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>


using namespace std;

#define frl(a, b, c) for( (a) = (b);( a) < (c); (a++))
#define fru(a, b, c) for( (a) = (b); (a) <= (c); (a++))
#define frd(a, b, c) for( (a) = (b); (a) >= (c); (a--))
#define mst(a, b) memset(a, b, sizeof(a))
#define si(a) scanf("%d", &a)
#define ss(a) scanf("%s", a)
#define sc(a) scanf("%c", &a)

#define pb(a) push_back(a)
#define mp make_pair
#define nwl puts("");
#define sp << " " <<

#define sz size()
#define bg begin()
#define en end()
#define X first
#define Y second

#define vi vector <int>
#define vs vector <string>
#define ll long long int
#define dec int i = 0, j= 0, k = 0;

#define i(n) cin >> n;
#define p(s) cout << s;

// 1 - 1
// i - 2
// j - 3
// k = 4

int a[1001];



int main(){
    int t, i, j, k, n;
    freopen("B-large.in", "r", stdin);
    freopen("outSmallB.txt", "w", stdout);
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        cin >> n;
        int mx = 0, mx2 = 0;
        frl(i, 0, n){
            cin >> a[i];
            mx = max(mx, a[i]);
        }
        ll ans = 1000000000000000000ll, curr = 0;
        frl(i, 1, mx + 1){
            curr = mx2 = 0;
            frl(j, 0, n){
                curr += (((a[j] + i - 1) / i) - 1);
                mx2 = max(mx2, (a[j] / i >= 1) ? i : (a[j] % i));
            }
            // cout << curr << " " << mx2 << endl;
            ans = min(ans, curr + mx2);
        }
        cout << "Case #" << tt << ": " << ans << endl;
    }
}







































