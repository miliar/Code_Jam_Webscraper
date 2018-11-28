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

string a[111];

int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
int n,m;
bool isOn(int x, int y)
{
	return (x>=0 && y>=0 && x<n && y<m);
}
bool isFindOnDir(int x, int y, int dir)
{
	x+=dirs[dir][0];
	y+=dirs[dir][1];
	if (!isOn(x,y))
		return false;
	if (a[x][y] != '.') {
		return true;
	}
	return isFindOnDir(x,y,dir);
}

int dirByChar[256];

int main() {
	FILES;
	ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	dirByChar['v'] = 2;
	dirByChar['^'] = 3;
	dirByChar['>'] = 0;
	dirByChar['<'] = 1;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #"<<test<<": ";
		cin >> n >> m;
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
		}
		bool bad = false;
		int res = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] != '.') {
					if (isFindOnDir(i,j,dirByChar[a[i][j]])) {
						continue;
					}
					else {
						bool any = false;
						for (int k = 0; k < 4; ++k) {

							if (isFindOnDir(i,j,k)) {
								any = true;
								break;
							}
						}
						if (!any)
							bad = true;
						else
							res++;
					}
				}
			}
		}
		if (bad)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << res << endl;
		}
	}

    return 0;
}