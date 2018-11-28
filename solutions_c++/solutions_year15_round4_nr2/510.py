#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

typedef long long Long;
typedef long double Double;
namespace Helper
{
    template<typename T> inline string inttos(T x){ostringstream q;q << x;return q.str();}
    inline int stoint( string str){istringstream in(str);int res;in >> res;return res;}
    inline Long stolong(string str){istringstream in(str);Long res;in >> res;return res;}
    template<typename T> inline T pow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
    template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}
    inline int rand() { long long q = 1ll*rand()*RAND_MAX+rand(); return q % INT_MAX; }
    inline int abs(int x) { if (x<0) return -x;else return x; }
    const int MAXINT = 0x7FFFFFFF;
}

#ifdef h0me
#define FILES freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILES
#endif

Double r[1111],c[1111];
int main() {
	FILES;
	ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #"<<test<<": ";
		Double v,x;
		int n;
		cin >> n >> v >> x;
		for (int i = 0; i < n; ++i) {
			cin >> r[i] >> c[i];
		}
		cout.precision(9);
		cout << fixed;

		if (n==2 && fabs(c[0]-c[1])<1e-6) {
			n = 1;
			r[0] += r[1];
		}
		//cout << "F" << endl;
		if (n==1) {
			if (abs(c[0]-x)<1e-7) {
				cout << v/r[0] << endl; 
			}
			else {
				cout << "IMPOSSIBLE" << endl;
			}
		}
		else {
			if (c[0]>c[1]) {
				swap(c[0],c[1]);
				swap(r[0],r[1]);
			}
			Double L = 0;
			Double R = v;
			for (int it = 0; it < 1000; ++it) {
				Double m = L+(R-L)/2;
				Double V0= m;
				Double V1= v-V0;
				Double q = (V1*c[1]+V0*c[0])/v;
				if (q>x)
					L = m;
				else R = m;
			}

			Double V0= L;
			Double V1=v-V0;
			Double res = max(V1/r[1],V0/r[0]);
			Double q = (V1*c[1]+V0*c[0])/v;
			if (abs(q-x)>1e-10) {
				cout << "IMPOSSIBLE" << endl;
			}
			else {
				cout << res << endl;
			}
			
		}
				
	}

    return 0;
}