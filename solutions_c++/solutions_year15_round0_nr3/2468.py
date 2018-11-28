#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iterator>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
//#include <utility>
//#include <memory>
//#include <functional>
//#include <deque>
//#include <cctype>
//#include <ctime>
//#include <numeric>
//#include <list>
//#include <iomanip>

//#if __cplusplus >= 201103L
//#include <array>
//#include <tuple>
//#include <initializer_list>
//#include <forward_list>
//
//#define cauto const auto&
//#else

//#endif

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
    v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
    stringstream ss;
    ss << f;
    ss >> t;
}


#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define F first
#define S second
#define mkp make_pair
#define RALL(v) (v).rbegin(),(v).rend()
// #define DEBUG
#ifdef DEBUG
#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#else
#define dump(x) 
#define debug(x) 
#endif

#define MOD 1000000007LL
#define EPS 1e-8
static const int INF=1<<24;
string s;
int dp1[10010];
int dp2[10010];
int n;
vint v;
int ijk(int a,int b){
	int t=a/abs(a);
	t*=b/abs(b);
	b=abs(b);
	if(abs(a)==1){
		return t*b;
	}
	if(abs(a)==2){
		if(b==1) return a*t;
		if(b==2) return -t;
		if(b==3) return 4*t;
		if(b==4) return -3*t;
	}
	if(abs(a)==3){
		if(b==1) return a*t;
		if(b==2) return -4*t;
		if(b==3) return -t;
		if(b==4) return 2*t;
	}
	if(abs(a)==4){
		if(b==1) return a*t;
		if(b==2) return 3*t;
		if(b==3) return -2*t;
		if(b==4) return -t;
	}
	return 0;
}
map<pii,int> ma;
int aa[2]={1,-1};
void mainmain(){
	reep(i,1,5){
		reep(j,1,5){
			rep(ii,2){
				rep(jj,2){
					int t=ijk(i*aa[ii],j*aa[jj]);
					ma[pii(j*aa[jj],t)]=i*aa[ii];
				}
			}
		}
	}
	int T;
	cin>>T;
	rep(o,T){
		cout<<"Case #"<<o+1<<": ";
		int a,b;
		cin>>a>>b;
		string t;
		cin>>t;
		s="";
		n=a*b;
		if(n<=2){
			puts("NO");
			continue;
		}
		rep(i,b) s+=t;
		v=vint(n);
		rep(i,n){
			v[i]=s[i]-'i'+2;
		}
		int tt=v[0];
		dp1[0]=tt;
		reep(i,1,n){
			dp1[i]=ijk(tt,v[i]);
			tt=dp1[i];
		}
		// cout<<"dp1 "<<endl;
		// cout<<endl;
		dp2[n-1]=v[n-1];
		tt=v[n-1];
		for(int i=n-2;i>=0;i--){
			dp2[i]=ijk(v[i],tt);
			tt=dp2[i];
		}
		bool f=false;
		rep(i,n-2){
			if(dp1[i]==2&&dp2[i+1]==2){
				reep(j,i+1,n){
					if(dp2[j]==4){
						f=true;
					}
				}
			}
		}
		if(f) puts("YES");
		else puts("NO");
	}
}


main() {
    mainmain();
}