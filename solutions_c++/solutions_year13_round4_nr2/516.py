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
	int n,p; cin>>n>>p;
	if((1<<n)==p){
		cout<<p-1<<' '<<p-1<<endl;
		return;
	}
	vi a(1<<n); iota(all(a),0);
	
	rep(i,n){
		vi b(1<<n);
		int m=1<<(n-i);
		for(int j=0;j<(1<<n);j+=m){
			for(int k=0;k<m;k++){
				if(k%2==0) b[j+k/2]=a[j+k];
				if(k%2==1) b[j+m/2+k/2]=a[j+k];
			}
		}
		a=b;
	}
	int any=*min_element(begin(a)+p,end(a))-1;
	int can=*max_element(begin(a),begin(a)+p);
	cout<<any<<' '<<can<<endl;
}

void solve()
{
	ll n,p; cin>>n>>p;
	if((1ll<<n)==p){
		cout<<p-1<<' '<<p-1<<endl;
		return;
	}
	
	ll a=0;
	for(ll i=1,j=1ll<<n-1;i<=p;i+=j,j>>=1)
		a=a*2+1;
	ll b=0;
	for(ll i=1,j=1;i<p;i+=1ll<<j,j++)
		b+=1ll<<n-j;
	
	ll any=a-1,can=b;
	cout<<any<<' '<<can<<endl;
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
