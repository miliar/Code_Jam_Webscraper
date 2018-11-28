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

typedef __int128 ull;

ull unsignedMillerRabinSuspectPow(__int128 a,__int128 k, __int128 n){
    ull p=1;
    __int128 bit;// 32bit
    for(bit=0x80000000U;bit;bit>>=1){
        if(p>1) p=(p*p)%n;
        if(k&bit) p=(p*a)%n;
    }
    return p;
}

bool unsignedMillerRabinSuspect(__int128 b, __int128 n){
    __int128 i,t=0,u=n-1;
    ull now,next;

    while(!(u&1)) t++,u>>=1;
    now = unsignedMillerRabinSuspectPow(b, u, n);

    for(i=1;i<=t;i++){
        next=(now*now)%n;
        if(next==1 && now!=1 && now!=n-1) return false;
        now=next;
    }
    return next==1;
}

bool unsignedMillerRabin(__int128 n){
    if(n<=1) return false;
    if(n<=3) return true;
    if(!(n&1)) return false;
    if(!unsignedMillerRabinSuspect(2,n)) return false;
    for(__int128 i=3;i<=51;i+=2) if(!unsignedMillerRabinSuspect(i,n)) return false;
    // if(n<=1000000){
    //     if(!unsignedMillerRabinSuspect(3,n)) return false;
    // }
    // else{
    //     if(!unsignedMillerRabinSuspect(7,n)) return false;
    //     if(!unsignedMillerRabinSuspect(61,n)) return false;
    // }
    return true;
}

class XorShift{
public:
    static int rand();
private:
    static unsigned int x;
    static unsigned int y;
    static unsigned int z;
    static unsigned int w;
    static unsigned int t;
};
unsigned int XorShift::x = 123456789;
unsigned int XorShift::y = 362436069;
unsigned int XorShift::z = 521288629;
unsigned int XorShift::w = 88675123;
unsigned int XorShift::t = 1;
 
int XorShift::rand(){
    t = x ^ (x << 11);
    x = y;
    y = z;
    z = w;
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    return w & 0x7fffffff;
}
void mainmain(){
	int T;
	cin >> T;
	set<__int128> used;
	XorShift ran;
	for(int o = 1;o <= T; o++){
		cout << "Case #" << o << ":" << endl;
		int n,m;
		cin >> n >> m;
		__int128 t = 1LL << (n-1);
		t++;
		int ad = 2520;
		int cnt = 1;
		// vint ans = {4,9,2,25,2,49,2,3,2};
		while(1){
			__int128 x = t + 1LL * ran.rand() % (1LL << (n-2)) * 2;
			// cout << "x " << x << endl;
			if(used.find(x) != used.end()) continue;
			vint ans;
			reep(i,2,11){
				// cout<< i<<endl;
				__int128 a = 1;
				__int128 b = 0;
				rep(j,n){
					if(x&(1LL<<j)) b += a;
					a *= i;
				}
				// cout << " i " << i << " b " << b << endl;
				if(unsignedMillerRabin(b)) break;
				__int128 div = 1;
				while(1){
					div++;
					if(div > 1000) break;
					// if(div == i) continue;
					if(b % div == 0){
						ans.PB(div);
						break;
					}
				}
			}
			if(ans.size() < 9) continue;
			rep(i,n){
				if(x & 1LL<<(n-1-i)) cout<<1;
				else cout<<0;
			}
			rep(i,ans.size()){
				cout<<" "<<ans[i];
			}
			cout<<endl;
			used.insert(x);
			if(++cnt > m) break;
		}
	}
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<fixed<<setprecision(20);
    mainmain();
}