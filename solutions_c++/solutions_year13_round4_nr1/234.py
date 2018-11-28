#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000002013LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

ll N,M,o[1010],e[1010],p[1010];
ll points[2222],K;
int from[1010],to[1010];
ll c[2222];

#define Sum(x) ((x)*((x)-1)/2)

void main2(){
	cin>>N>>M;
	rep(i,M)cin>>o[i]>>e[i]>>p[i];
	
	ll init=0;
	rep(i,M){
		init += Sum(e[i]-o[i])%MOD*p[i]%MOD;
	}
	init%=MOD;
	
	set<ll> S;
	rep(i,M){
		S.insert(o[i]);
		S.insert(e[i]);
	}
	K=0;
	foreach(it,S){
		points[K++]=*it;
	}
	memset(c,0,sizeof(c));
	rep(i,M){
		from[i] = lower_bound(points,points+K,o[i])-points;
		to[i] = lower_bound(points,points+K,e[i])-points;
		rep2(j,from[i],to[i])c[j]+=p[i];
	}
	
	ll ans=0;
	while(1){
		int ok=1;
		rep(i,K)if(c[i]){ok=0;break;}
		if(ok)break;
		//rep(i,K)cout<<c[i]<<" ";cout<<endl;
		
		ll mini=INF*INF;
		ll len=0;
		int start=-1;
		rep(i,K){
			if(!c[i]){
				if(start!=-1){
					ans+=Sum(len)%MOD *mini%MOD;
					//cout<<"+"<<Sum(len)%MOD *mini%MOD<<endl;
					rep2(j,start,i)c[j]-=mini;
				}
				mini=INF*INF;
				len=0;
				start=-1;
			}else{
				mini=min(mini,c[i]);
				len += points[i+1]-points[i];
				if(start==-1)start=i;
			}
		}
	}
	ans%=MOD;
	cout<<(ans-init+MOD)%MOD<<endl;
}

int main(){
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
