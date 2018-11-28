//Satyam Pandey//
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long int LL;

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
  cerr<<name<<" : "<<arg1<<endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names,Arg1&& arg1,Args&&... args){
  const char* comma=strchr(names+1,',');
  cerr.write(names,comma-names)<<" : "<<arg1<<" | ";__f(comma+1,args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
int a[10],cnt;
inline void mark(LL v)
{
	while(v!=0){
		if(!a[v%10])
			cnt++,a[v%10]=1;
		v/=10;
	}
}
int main()
{
	int t;si(t);
	for(int tt=0;tt<t;tt++)
	{
		LL n,v;
		sll(n);
		SET(a,0);
		cnt=0;v=n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",tt+1);
			continue;
		}
		while(cnt<10){
			mark(v);
			v+=n;
		}
		printf("Case #%d: %lld\n",tt+1,v-n);
	}
	return 0;
}
