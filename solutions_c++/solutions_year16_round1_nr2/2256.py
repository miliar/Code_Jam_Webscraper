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
#include <fstream>
#include <iomanip>
#include <cassert>
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
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define maxs(x,y) x=max(x,y)
#define mins(x,y) x=min(x,y)

vvint e;
set<int> used;
int n;
vvint vv;
vint depth;
vint ans;

bool check(vint &a,vint &b){
	rep(i,a.size()){
		if(a[i]>b[i]) return false;
	}
	return true;
}

bool check2(){
	vint a;
	vint b;
	rep(i,2*n-1){
		if(used.find(i)!=used.end()){
			a.PB(i);
		}
		else{
			b.PB(i);
		}
	}
	// cout<<"check 2"<<endl;
	vvint aa;
	vvint bb;
	rep(i,a.size()){
		aa.PB(vv[a[i]]);
	}
	rep(i,b.size()){
		bb.PB(vv[b[i]]);
	}
	sort(ALL(aa));
	sort(ALL(bb));
	vvint tmp;
	initvv(tmp,n,n);
	rep(i,n){
		rep(j,n){
			tmp[i][j] = aa[i][j];
		}
	}
	// cout<<"aa"<<endl;
	vint tt;
	int pos = 0;
	rep(i,n){
		bool ok = true;
		if(pos == n-1){
			tt.PB(n-1);
			break;
		}
		rep(j,n){
			// cout<<j<<" "<<pos<<endl;
			if(bb[pos][j] != tmp[j][i]){
				ok=false;
			}
		}
		if(!ok){
			tt.PB(i);
		}
		else{
			pos++;
		}
	}

	// rep(i,tmp.size()){
	// 	rep(j,tmp[i].size()){
	// 		cout<<tmp[i][j]<<" ";
	// 	}
	// 	cout<<endl;
	// }
	// rep(i,a.size()){
	// 	cout<<a[i]<<" ";
	// }
	// cout<<endl;
	// rep(i,b.size()){
	// 	cout<<b[i]<<" ";
	// }
	// cout<<endl;
	// cout<<"bb "<<tt[0]<<endl;
	if(tt.size()==1){
		ans = vint(n);
		rep(i,n){
			// cout<<i<<endl;
			ans[i] = tmp[i][tt[0]];
		}
		return true;
	}
	return false;
}

bool dfs(int x){
	used.insert(x);
	// cout<<"x "<<x<<" "<<used.size()<<endl;
		
	if(used.size() == n){
		if(check2()) return true;
		// cout<<"check 2 end"<<endl;
		used.erase(x);
		return false;
	}
	// cout<<"a "<<vv[x].size()<<endl;
	for(int y:e[x]){
		// if(depth[y]+1+used.size() < n) continue;
		if(used.find(y)!=used.end()) continue;
		// cout<<"y "<<y<<" "<<x<<endl;
		if(dfs(y)) return true;
	}
	used.erase(x);
	return false;
}


void mainmain(){
	int T;
	cin >> T;
	rep(o,T){
		used.clear();

		cout<<"Case #"<<o+1<<": ";
		cin >> n;
		initvv(vv,2*n-1,n);
		e=vvint(2*n-1);
		rep(i,vv.size()){
			rep(j,n){
				cin>>vv[i][j];
			}
		}
		vvint aa;
		initvv(aa,2*n-1,2*n-1,INF);
		rep(i,2*n-1){
			rep(j,2*n-1){
				if(i==j) continue;
				if(check(vv[i],vv[j])){
					e[i].PB(j);
					aa[i][j]=1;
				}
			}
		}
		rep(k,aa.size()){
			rep(i,aa.size()){
				rep(j,aa.size()){
					mins(aa[i][j],aa[i][k]+aa[k][j]);
				}
			}
		}
		depth=vint(2*n-1,0);
		rep(i,2*n-1){
			rep(j,2*n-1){
				if(aa[i][j]==INF) continue;
				maxs(depth[i],aa[i][j]);
			}	
			// cout<<"depth "<<i<<" "<<depth[i]<<endl;		
		}
		rep(i,2*n-1){
			if(dfs(i)){
				rep(j,ans.size()){
					if(j) cout<<" ";
					cout<<ans[j];
				}
				cout<<endl;
				break;
			}
		}
		// sort(ALL(vv));
		// rep(i,vv.size()){
		// 	rep(j,vv[i].size()){
		// 		cout<<vv[i][j]<<" ";
		// 	}
		// 	cout<<endl;
		// }
		// cout<<endl;
	}
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<fixed<<setprecision(20);
    mainmain();
}