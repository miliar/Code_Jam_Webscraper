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

vvint vv;

int dfs(int x,int y=-1){
	int ret=0;
	rep(i,vv[x].size()){
		if(vv[x][i] == y) continue;
		maxs(ret,dfs(vv[x][i])+1);
	}
	return ret;
}


void mainmain(){
	int T;
	cin>>T;
	rep(o,T){
		cout<<"Case #"<<o+1<<": ";
		int n;
		cin>>n;
		vint v(n);
		rep(i,n) cin>>v[i],v[i]--;
		int ans = 0;
		rep(i,n){
			set<int> used;
			int pos = i;
			while(1){
				if(used.find(pos)!=used.end()) break;
				used.insert(pos);
				pos=v[pos];
			}
			if(pos!=i) continue;
			maxs(ans,(int)used.size());
		}
		vv=vvint(n);
		rep(i,n){
			vv[v[i]].PB(i);
		}
		int tmp = 0;
		vint t;
		rep(i,n){
			rep(j,i){
				if(v[i]==j&&v[j]==i){
					// cout<<i<<" "<<j<<endl;
					int a=max(dfs(i,j),dfs(j,i));
					int b=min(dfs(i,j),dfs(j,i));
					tmp+=a+2;
					t.PB(b);
				}
			}
		}
		sort(ALL(t));
		if(t.size()>=2) tmp+=t[t.size()-2];
		if(t.size()) tmp+=t.back();
		cout<<max(ans,tmp)<<endl;
	}
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<fixed<<setprecision(20);
    mainmain();
}