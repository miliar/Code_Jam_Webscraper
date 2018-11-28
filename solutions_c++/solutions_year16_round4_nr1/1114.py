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
int cnt[3],n,L[3],R[3];
string dp[13][3];
bool ok[13][3];
char C[3];map<char,int> mp;
void solve(int l,int r){
  if(ok[l][r])return;
  if(l==0){
    dp[l][r] = "";
    dp[l][r] += C[r];
    ok[l][r] = true;
    return;
  }
  solve(l-1,L[r]);
  solve(l-1,R[r]);
  dp[l][r] = min(dp[l-1][L[r]]+dp[l-1][R[r]],dp[l-1][R[r]]+dp[l-1][L[r]]);
  ok[l][r] = true;
  return;
}
bool check(int i){
  int c[3];
  for(int i=0;i<3;i++)c[i]=cnt[i];
  for(auto cc:dp[n][i])c[mp[cc]]--;
  for(int i=0;i<3;i++)if(c[i]<0)return false;
  return true;
}
int main()
{
  int t;si(t);
  C[0]='P';C[1]='R';C[2]='S';
  mp['P']=0;mp['R']=1;mp['S']=2;
  L[0]=0;L[1]=1;L[2]=2;
  R[0]=1;R[1]=2;R[2]=0;
  for(int i=0;i<13;i++)
    for(int j=0;j<3;j++)
      solve(i,j);
  for(int T=1;T<=t;T++){
    printf("Case #%d: ",T);si(n);
    scanf("%d %d %d",cnt+1,cnt,cnt+2);
    string ans = "z";
    for(int i=0;i<3;i++)
      if(ok[n][i] && check(i))
        ans = min(ans,dp[n][i]);
    if(ans=="z")puts("IMPOSSIBLE");
    else cout<<ans<<endl;
  }
	return 0;
}
