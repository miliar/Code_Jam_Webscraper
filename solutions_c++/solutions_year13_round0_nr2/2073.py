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
#define max 105
int n,m;
int arr[max][max];
bool vis[max][max];
bool hav[max];
bool solve()
{
    clr(vis);
    repp(x,1,101)if(hav[x])
    {
        rep(i,n)rep(j,m)if(!vis[i][j]&&arr[i][j]==x)
        {
            bool r=1,c=1;
            rep(k,n)if(arr[k][j]>x)
            {
                c=0;
                break;
            }
            if(c)rep(k,n)vis[k][j]=1;
            rep(k,m)if(arr[i][k]>x)
            {
                r=0;
                break;
            }
            if(r)rep(k,m)vis[i][k]=1;
            if(r==0&&c==0)return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        clr(hav);
        rep(i,n)rep(j,m)
        {
            cin>>arr[i][j];
            hav[arr[i][j]]=1;
        }
        printf("Case #%d: ",cas++);
        if(solve())puts("YES");
        else puts("NO");
    }
	return 0;
}
