//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <queue>
#include <climits>
#include <cassert>
using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> pii;
typedef long long ll;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define fi first
#define se second

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const int dx[] = {-1,1,0,0};
const int dy[] = {0,0,1,-1};

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int T, n, l, ret;
string a[210], b[210], c[210]; 
set<string> s;

/*
void small(){
    ret = 1000;
    s.clear();
    printf("Case #%d: ", t);
    cin >> n >> l;
    rep(i, n) cin >> a[i];
    rep(i, n){
	cin >> b[i];
	s.insert(b[i]);
    }

    rep(i, 1 << l){
	rep(j, n){
	    c[j] = a[j];
	    rep(k, l){
		if((i >> k) & 1){
		    if(c[j][k] == '1') c[j][k] = '0';
		    else c[j][k] = '1';
		}
	    }
	}

	set<string> d;
	rep(j, n) d.insert(c[j]);

	if(s == d) ret = min(ret, __builtin_popcount(i));
    }

}*/

int main(){
    cin >> T;

    for(int t = 1; t <= T; ++t){
	printf("Case #%d: ", t);
	ret = 1000;
	cin >> n >> l;
	s.clear();

	rep(i, n) cin >> a[i];
	rep(i, n){
	    cin >> b[i];
	    s.insert(b[i]);
	}

	//a[0] - b[i]

	rep(i, n){
	    int x = 0;
	    vector<int> v;
	    rep(j, l){
		if(b[i][j] != a[0][j]){
		    v.pb(1);
		    ++x;
		}
		else v.pb(0);
	    }

	    rep(j, n){
		c[j] = a[j];
		rep(k, v.size()){
		    if(v[k] == 1){
			if(c[j][k] == '1') c[j][k] = '0';
			else c[j][k] = '1';
		    }
		}
	    }
	    set<string> d;
	    rep(j, n){
		d.insert(c[j]);
	    }
	    if(d == s) ret = min(ret, x);
	}

	if(ret == 1000) puts("NOT POSSIBLE");
	else cout << ret << endl;
    }    
    return 0;
}
