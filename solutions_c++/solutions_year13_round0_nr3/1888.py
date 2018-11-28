#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define repp(i,a,n) for(int i=(a);i<(n);i++)
#define dec(i,n) for(int i=(n);i>0;i--)
#define decc(i,a,n) for(int i=(a);i>(n);i--)
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define abs(a) ((a)<0?-(a):(a))
#define sqr(a) ((a)*(a))
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
const double pi=acos(-1.0);
const int inf=10000000;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;
typedef vector< string > VS;
typedef vector< ll > VLL;
#define eps 1e-9
//main code starts here
ll ans[]=
{
1ll
,4ll
,9ll
,121ll
,484ll
,10201ll
,12321ll
,14641ll
,40804ll
,44944ll
,1002001ll
,1234321ll
,4008004ll
,100020001ll
,102030201ll
,104060401ll
,121242121ll
,123454321ll
,125686521ll
,400080004ll
,404090404ll
,10000200001ll
,10221412201ll
,12102420121ll
,12345654321ll
,40000800004ll
,1000002000001ll
,1002003002001ll
,1004006004001ll
,1020304030201ll
,1022325232201ll
,1024348434201ll
,1210024200121ll
,1212225222121ll
,1214428244121ll
,1232346432321ll
,1234567654321ll
,4000008000004ll
,4004009004004ll
,10000000000000000ll
};
int solve(ll a)
{
    rep(i,40)if(ans[i]>a)return i;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    int t,cas=1;
    ll a,b;
    cin>>t;
    while(t--)
    {
        cin>>a>>b;
        printf("Case #%d: %d\n",cas++,solve(b)-solve(a-1));
    }
	return 0;
}
