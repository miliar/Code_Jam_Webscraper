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
	static ll n,d;
	static ll s[1000010],m[1000010],a,c,q;
	static ll imos[1000010];
	static ll l[1000010],r[1000010];
	rep1(ppp,T){
		rep(i,1000010){
			imos[i] = 0;
			l[i] = 0;
			r[i] = 1000000;
		}
		printf("Case #%d: ",ppp);
		scanf("%lld%lld",&n,&d);
		scanf("%lld%lld%lld%lld",&s[0],&a,&c,&q);
		rep1(i,n-1){
			s[i] = (s[i-1]*a+c)%q;
		}
		scanf("%lld%lld%lld%lld",&m[0],&a,&c,&q);
		rep1(i,n-1){
			m[i] = (m[i-1]*a+c)%q;
		}
		rep1(i,n-1){
			m[i] %= i;
		}
		l[0] = max ( (ll)0 , s[0]-d );
		r[0] = min ( (ll)1000000 , s[0] );
		imos[l[0]] ++;
		imos[r[0]+1] --;
		rep1(i,n-1){
			l[i] = max( l[m[i]] , max ( (ll)0 , s[i]-d ) );
			r[i] = min( r[m[i]] , min ( (ll)1000000 , s[i] ) );
			if(l[i] > r[i])r[i] = l[i]-1;
			imos[l[i]] ++;
			imos[r[i]+1] --;
		}
		ll ret = imos[0];
		rep1(i,1000009){
			imos[i] += imos[i-1];
			ret = max ( ret , imos[i] );
		}
		printf("%lld\n",ret);
	}
}
		
		

