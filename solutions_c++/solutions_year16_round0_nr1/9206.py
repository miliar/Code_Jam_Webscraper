/*
Farsid
BUET
*/

#include <bits/stdc++.h>
using namespace std;

#define SET(a, x) memset((a), (x), sizeof(a))
#define ll long long
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define i64 ll
#define IN(A, B, C)  ((B) <= (A) && (A) <= (C))
#define MAX
#define xx first
#define yy second

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<ll> VL;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
const int inf=0x20202020;
const ll linf=(((i64)1)<<60)-1;
const ll mod=1000000007;
const double eps=1e-9;
const double pi=3.1415926535897932384626;

const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
ll inv_mod(ll a,ll mod){return powmod(a,mod-2,mod);}



int solve(int n)
{
    //SET(vst,0);
    int vst=0;
    int cnt=1;
    while(1){
        int m=cnt*n;
        while(m){
            int d=m%10;
            m/=10;
            vst|=(1<<d);
        }
        if(vst==(1<<10)-1)break;
        cnt++;
    }
    return cnt;

}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("gadha.out","w",stdout);
    int i,j,T,cas=0;
    /*int mx=0;
    for(i=1;i<=1000000;i++){
        mx=max(mx,solve(i));
    }
    cout<<mx<<endl;*/
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++cas);
        int n;
        scanf("%d",&n);
        if(!n){
                cout<<"INSOMNIA"<<endl;
                continue;
        }
        int x=solve(n);
        cout<<x*n<<endl;
    }
    return 0;
}
/*Test Cases


*/
