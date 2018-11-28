#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int mo=1000000007;
int sum[114],pat[10];
int m,n,ma;
string s[10];
void cal(int a){
	vector<string> v[5];
	int su=0,pl=1;
	rep(i,m){
		rep(j,s[i].size()+1) v[pat[i]].pb(s[i].substr(0,j));
	}
	rep(i,a){
		if(v[i].size()<1) continue;
		sort(All(v[i]));v[i].erase(unique(All(v[i])),v[i].end());
		su+=v[i].size();
	}
	ma=max(ma,su);
	rep(i,a) pl*=n-i;
	sum[su]+=pl;sum[su]%=mo;
}
void dfs(int a,int b){
	if(a==m){
		cal(b);return;
	}
	rep(i,b){
		pat[a]=i;dfs(a+1,b);
	}
	if(b<n){
		pat[a]=b;dfs(a+1,b+1);
	}
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cin>>m>>n;
		rep(j,m) cin>>s[j];
		ma=0;memset(sum,0,sizeof(sum));
		dfs(0,0);
		printf("Case #%d: %d %d\n",i+1,ma,sum[ma]%mo);
	}
}
