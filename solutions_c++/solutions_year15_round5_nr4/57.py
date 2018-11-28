#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int main(){
	int T;
	cin >> T;
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		ll p,e[10010],f[10010];
		scanf("%lld",&p);
		rep(i,p){
			scanf("%lld",&e[i]);
		}
		rep(i,p){
			scanf("%lld",&f[i]);
		}
		map<ll,ll> M;
		rep(i,p){
			M[e[i]] = i;
		}
		ll g[10010] = {};
		g[M[0]] = 1;
		vector<ll> ans;
		while(1){
			int v = -1;
			rep(i,p){
				if(f[i] > g[i]){
					v = i;
					break;
				}
			}
			if(v == -1)break;
			ans.pb(e[v]);
			rrep(i,p){
				if(g[i] == 0)continue;
				g[M[e[i]+e[v]]] += g[i];
			}
		}
		sor(ans);
		rep(i,ans.size()){
			printf("%lld%c",ans[i],(i==ans.size()-1)?'\n':' ');
		}
	}
}

