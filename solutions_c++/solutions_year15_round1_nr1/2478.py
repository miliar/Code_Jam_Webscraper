//============================================================================//
//------------------------>Nguyen Quoc Nhan<----------------------------------//
//--------------------->quocnhan1843@gmail.com<-------------------------------//
//============================================================================//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define oo 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932
#define MaxN 1000000

int GCD(int a, int b){return(b==0?a:GCD(b,a%b));}
int LCM(int a, int b){return a*(b/GCD(a,b));}

ll T, a[1000000 + 5], n, t = 1LL;
ll cnt1, cnt2;

int main(){

    #ifndef ONLINE_JUDGE
    freopen("INPUT.INP", "r", stdin);
    freopen("OUTPUT.OUT", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> T;

    while(T--){
            cnt1= cnt2 = 0LL;
        cin >> n;
        rep(i,n){
            cin >> a[i];
        }
        ll v = -1;
        fr(i,1,n-1){
            if(a[i] < a[i-1]){
                    cnt1 += a[i-1] - a[i];
                    v = max(v , a[i-1] - a[i]);
            }
        }
        //debug(v);
        rep(i,n-1){
            //debug(cnt2);
            if(a[i] >= v) cnt2+=v;
            else cnt2 += a[i];
        }
        printf("Case #%lld: %lld %lld\n", t++, cnt1, max(cnt2,0LL) );
    }

return 0;
}
