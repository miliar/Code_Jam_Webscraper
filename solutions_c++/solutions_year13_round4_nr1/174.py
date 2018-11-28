#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<string.h>
#include<set>
#include<map>
using namespace std;

typedef long long Int;
#define FOR(i,a,b)  for(int i=(a);i<=(b);++i)
#define sz(s) (int)(s).size()
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
void assert(bool x){if(!x)throw -1;}
const int inf = 1000000000;
const int MOD = 1000002013;
const double pi = acos(-1.0);
const Int INF = inf*(Int)inf;

set<int> city;
map<int,int> mem;
vector<int>c;

Int s[22111],f[22111],p[22111];
Int out[22211],tmp[22222];


Int get(int from,int to,Int n){
	if(from==to)return 0;
	Int mn = INF;
	FOR(i,from,to-1)mn=min(mn,out[i]);
	Int len = c[to]-c[from];
	Int cost1 = (2*n-len+1)*len/2;
	cost1%=MOD;
	Int cost = (mn*cost1)%MOD;
	for(int i=from;i<to;++i)out[i]-=mn;
	for(int i=from;i<to;++i)if(out[i]==0)return (cost+0LL+get(from,i,n)+get(i+1,to,n))%MOD;
}

int solve(){
	int n,m;
	cin>>n>>m;
	city.clear();
	mem.clear();
	Int total = 0;
	FOR(i,1,m){
		cin>>s[i]>>f[i]>>p[i];
		city.insert(s[i]);
		city.insert(f[i]);
		Int len = f[i]-s[i];
		Int cur = ((2*n-len+1)*len/2)%MOD;
		total=(total+cur*p[i])%MOD;
	}

	c.clear();
	for(set<int>::iterator it=city.begin();it!=city.end();++it){
		mem[*it]=sz(c);
		c.pb(*it);
	}
	Int have=0;
	memset(tmp,0,sizeof(tmp));
	FOR(i,1,m){
		tmp[mem[s[i]]]+=p[i];
		tmp[mem[f[i]]]-=p[i];
	}
	FOR(i,0,sz(c)-1){
		have+=tmp[i];
		out[i]=have;
	}
	Int best = get(0,sz(c)-1,n);
	return (total-best+MOD)%MOD;
}


int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","wb",stdout);
	int tests;
	scanf("%d\n",&tests);
	for(int test_id=1;test_id<=tests;++test_id){
		int ans = solve();
		cout<<"Case #"<<test_id<<": "<<ans<<endl;
	}
}  