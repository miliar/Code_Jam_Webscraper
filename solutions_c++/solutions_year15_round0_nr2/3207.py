#define filer() freopen("far.in","r",stdin)
#define filew() freopen("outB.txt","w",stdout)

#include <set>
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include <map>
#include<ctime>
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
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<ll> VL;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
const int inf=0x20202020;
const ll mod=1000000007;
const double eps=1e-9;
const double pi=3.1415926535897932384626;

const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}


template<class X>void debug(vector<X>&v){for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;}

int A[1010];

int main()
{
    //filer();
    freopen("B-large.in","r",stdin);
    filew();
    int i,j,k ,T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%d",&A[i]);
        int ans=2000;
        for(i=1000;i>=1;i--)
        {
            int mn=0;
            for(j=0;j<n;j++)
            {
                if(A[j]%i)mn+=(A[j]/i);
                else mn+=((A[j]/i)-1);
            }
            ans=min(ans,mn+i);
        }
        printf("Case #%d: %d\n",++cas,ans);

    }
    return 0;
}
/*Test Cases


*/
