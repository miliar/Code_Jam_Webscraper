#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

#define in

typedef long long LL;

#define For(i,b) for(i=0;i<b;i++)
#define Foru(i,a,b) for(i=a;i<=b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define mod 1000000007
double nao[1010],ken[1010];
void solve(){
    int t, n, ans1, ans2, p, q;
    int i, j, cnt;
    cin >> t;
    //cout<<setw(7) << setiosflags(ios::left)<< endl;;
    For(cnt,t){
        cin >> n;
        For(i,n) cin >> nao[i];
        For(i,n) cin >> ken[i];
        sort(nao,nao+n);
        sort(ken,ken+n);
        //For(i,n) cout << setw(7)<<nao[i] << ' ' ; cout << endl;
        //For(i,n) cout << setw(7)<<ken[i] << ' ' ; cout << endl;
        q = p = -1;
        ans1 = ans2 = 0;
        For(i,n){
            q = upper_bound(nao+q+1,nao+n,ken[i]) - nao;
            if(q<n) ans2++;
            p = upper_bound(ken+p+1,ken+n,nao[i]) - ken;
            if(p<n) ans1 ++;
           // cout << ken[p] << endl;
        }
        cout << "Case #" << cnt+1 << ": " << ans2 << ' ' << n-ans1 << endl;
    }
}
int main(){
    #ifdef in
        freopen("in","r",stdin);
        freopen("out","w",stdout);
    #endif
    solve();
    return 0;
}
