#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define fi first
#define se second
#define sr(x) (int)x.size()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define Bit(s,i) (((s)&(1<<(i)))>0)
#define Two(x) (1<<(x))
const int MOD = 1000000007;
const int nmax = 10000;
const double E = 1e-5;
const double PI = acos(-1);
typedef long long LL;
typedef pair<int,int> pii;
int n,m,stest;
double r[nmax],c[nmax], R, C;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> stest;
	For(test,1,stest) {
		cout << "Case #" << test << ": ";
		cin >> n >> R >> C;
		For(i,1,n) {
			cin >> r[i] >> c[i];
		}
		if ( n == 1 ) {
			if ( abs(c[1] - C) <= E ) printf("%.9lf", R / r[1]);
			else cout << "IMPOSSIBLE";
		} else {
			double t = C * R - R * c[1];
			double k = r[2] * c[2] - r[2] * c[1];
			if ( abs(c[1] - c[2]) <= E ) {
				if ( abs(c[1] - C) <= E ) {
					printf("%.9lf", R / (r[1] + r[2]) );
				} else cout << "IMPOSSIBLE";
			} else 
			{
				double X2 = t/k;
				double X1 = (R - r[2] * X2) / r[1];
				if ( X1 < -E || X2 < -E ) cout << "IMPOSSIBLE";
				else printf("%.9lf", max(X1,X2) );
			}
		}
		cout << endl;
	}
	return 0;
}