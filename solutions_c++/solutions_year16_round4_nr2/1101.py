//Tanuj Khattar
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
const int N = 201;
double dp[N][N],P[N],cnt[N],ans;
int n,k;
VI x;
void get(int pos){
  if(pos == n+1){
    if(SZ(x)!=k)return;
    for(int i=0;i<=n;i++)
      for(int j=0;j<=n;j++)
        dp[i][j]=0;
    dp[0][0]=1-P[x[0]];
    dp[0][1]=P[x[0]];
    for(int i=1;i<SZ(x);i++)
      for(int j=0;j<=i+1;j++)
        dp[i][j] = dp[i-1][j]*(1-P[x[i]]) + (j?dp[i-1][j-1]*P[x[i]]:0);
    ans = max(ans,dp[SZ(x)-1][k/2]);
    return;
  }
  get(pos+1);
  x.PB(pos);get(pos+1);x.pop_back();
}
int main()
{
  int t;si(t);
  for(int T = 1;T<=t;T++){
    printf("Case #%d: ",T);
    si(n);si(k);
    for(int i=1;i<=n;i++)
      scanf("%lf",P+i);
    ans = -1e12;get(1);
    printf("%.8lf\n",ans);
  }
	return 0;
}
