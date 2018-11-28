#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <functional>
#include <iterator>

using namespace std;

#define dump(n) cout<<"# "<<#n<<'='<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int INFTY=1<<29;
const double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a){
	os<<'[';
	rep(i,a.size()) os<<(i?" ":"")<<a[i];
	return os<<']';
}

void solve_naive()
{
	int n,m; cin>>n>>m;
	vi os;
	map<int,int> es;
	ll sum1=0;
	rep(i,m){
		int o,e,p; cin>>o>>e>>p;
		int d=e-o;
		sum1+=(d*n-d*(d-1)/2)*p;
		rep(j,p) os.push_back(o);
		es[e]+=p;
	}
	
	sort(all(os),greater<int>());
	
	ll sum2=0;
	rep(i,os.size()){
		auto j=es.lower_bound(os[i]);
		int d=j->first-os[i];
		sum2+=d*n-d*(d-1)/2;
		j->second--;
		if(j->second==0) es.erase(j);
	}
	
	cout<<sum1-sum2<<endl;
}

void solve()
{
	solve_naive();
}

int main()
{
	int T; scanf("%d",&T);
	rep(i,T){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
