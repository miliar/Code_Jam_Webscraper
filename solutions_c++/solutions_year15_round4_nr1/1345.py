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

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define F first
#define S second
#define mkp make_pair
#define RALL(v) (v).rbegin(),(v).rend()
#define DEBUG
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
int dx[]={0,1,0,-1};
int dy[]={-1,0,1,0};
string no="IMPOSSIBLE";
bool check(int a,int b,int c,int d){
	if(0<=a&&a<c&&0<=b&&b<d) return true;
	return false;
}
void mainmain(){
	int T;
	cin>>T;
	rep(o,T){
		cout<<"Case #"<<o+1<<": ";
		int h,w;
		cin>>h>>w;
		vvint vv;
		initvv(vv,h,w);
		rep(i,h){
			rep(j,w){
				char t;
				cin>>t;
				if(t=='^') vv[i][j]=0;
				else if(t=='>')	vv[i][j]=1;
				else if(t=='v') vv[i][j]=2;
				else if(t=='<') vv[i][j]=3;
				else if(t=='.') vv[i][j]=4;
			}
			// cout<<endl;
		}
		int ans=0;
		bool f=true;
		rep(i,h){
			rep(j,w){
				int tmp=0;
				if(vv[i][j]==4) continue;
				rep(k,h){
					if(i==k) continue;
					if(vv[k][j]!=4) tmp++;
				}
				rep(k,w){
					if(j==k) continue;
					if(vv[i][k]!=4) tmp++;
				}
				if(tmp==0) f=false;
			}
		}
		rep(i,h){
			rep(j,w){
				if(vv[i][j]!=4){
					bool ff=false;
					int y=i+dy[vv[i][j]];
					int x=j+dx[vv[i][j]];
					while(1){
						// cout<<y<<" "<<x<<endl;
						if(!check(y,x,h,w)) break;
						if(vv[y][x]!=4){
							ff=true;
							break;
						}
						y+=dy[vv[i][j]];
						x+=dx[vv[i][j]];
					}
					if(ff) continue;
					else ans++;
				}
			}
		}
		if(!f) cout<<no<<endl;
		else cout<<ans<<endl;
	}
}


signed main() {
    mainmain();
}