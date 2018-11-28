#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
// inhortcuts for "common" data types in contests
#define ll long long
#define pb push_back
#define pii pair <int ,char>
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define rep(i, a, b) for(ll i=a; i<b; i++)
#define ALL(c) c.begin(), c.end()
#define rloop(i, a, b) for(int i=b-1; i>=a; i--)
#define loopinc(i, a, b, inc) for(int i=a; i<b; i+=inc)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
 
//   freopen("ain.txt","r",stdin); freopen("aout.txt","w",stdout);




ll modPow(ll a, ll x, ll p) {
    //calculates a^x mod p in logarithmic time.
    ll res = 1;
    while(x > 0) {
        if( x % 2 != 0) {
            res = (res * a) % p;
        }
        a = (a * a) % p;
        x /= 2;
    }

    return res;
}int main()
{
    freopen("bin.txt","r",stdin); freopen("bout.txt","w",stdout);
    int tt, T, n;
    long long m, s;
    int arr[60][60], i, j;
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%d %lld", &n, &m);
        s=1;
        for(i=1; i<=n-2; ++i) s*=2;
        if(m>s) { printf("Case #%d: IMPOSSIBLE\n", tt); 
    continue; 
}
        printf("Case #%d: POSSIBLE\n", tt);
        for(i=1; i<=n; ++i)
        {
            for(j=1; j<=i; ++j) arr[i][j]=0;
            for(j=i+1; j<n; ++j) arr[i][j]=1;
        }
        if(m==s)
        {
            for(i=1; i<n; ++i) arr[i][n]=1;
        }
        else
        {
            arr[1][n]=0;
            for(i=2; i<n; ++i)
            {
                arr[i][n]=(m%2);
                m/=2;
            }
        }
        for(i=1; i<=n; ++i)
        {
            for(j=1; j<=n; ++j)
            {
                printf("%d", arr[i][j]);
            }
            printf("\n");
        }
    }
}