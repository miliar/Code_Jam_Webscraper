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
#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
#define all(c) begin(c),end(c)
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
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

void solve()
{
	double c,f,x; cin>>c>>f>>x;
	
	double cps=2;
	double res=0;
	for(;;){
		double t0=x/cps;
		double t1=c/cps;
		cps+=f;
		double t2=x/cps;
		if(t0<t1+t2){
			res+=t0;
			break;
		}
		res+=t1;
	}
	printf("%.7f\n",res);
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
