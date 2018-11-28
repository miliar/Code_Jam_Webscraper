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
int num[1010];
bool dp[17][(1<<15)+10];
string s[1010];
int main()
{
	int t,n;
	cin>>t;
	rep(i,t){
		cin>>n;
		rep(j,n){
			cin>>s[j];cin>>num[j];num[j]--;
		}
		vector<int> v;
		rep(j,n){
			if(num[j]>=0) v.pb(num[j]);
		}
		//cout<<v.size()<<endl;
		if(v.size()>0){sort(All(v));v.erase(unique(All(v)),v.end());}
		rep(j,n){
			if(num[j]>=0) num[j]=lower_bound(All(v),num[j])-v.begin();
		}
		rep(j,n){if(num[j]>=n) cerr<<-1<<endl;}
		memset(dp,false,sizeof(dp));
		rep(j,(1<<n)) dp[0][j]=true;
		rep(j,n) rep(k,(1<<n)){
			if(!dp[j][k]) continue;
			if(num[j]<0){
				rep(l,n){
					if((k&(1<<l)) && s[j]=="L") dp[j+1][k-(1<<l)]=true;
					if(!(k&(1<<l)) && s[j]=="E") dp[j+1][k+(1<<l)]=true;
				}
			}
			else{
				if((k&(1<<num[j])) && s[j]=="L") dp[j+1][k-(1<<num[j])]=true;
				if(!(k&(1<<num[j])) && s[j]=="E") dp[j+1][k+(1<<num[j])]=true;
			}
		}
		int ret=20;
		rep(j,(1<<n)){
			if(dp[n][j]) ret=min(ret,__builtin_popcount(j));
		}
		if(ret>=20) printf("Case #%d: CRIME TIME\n",i+1);
		else printf("Case #%d: %d\n",i+1,ret);
	}
}
