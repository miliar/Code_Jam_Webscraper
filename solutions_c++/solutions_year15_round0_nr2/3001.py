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
const double E = 1e-8;
const double PI = acos(-1);
typedef long long LL;
typedef pair<int,int> pii;
int n,m,stest,a[nmax];

int main() {
	freopen("input1.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin >> stest;
	For(test,1,stest) {
		cin >> n;
		For(i,1,n) {
			cin >> a[i];
		}
		int res = MOD;
		For(i, 1, 1000 ) {
			int ans = 0;
			For(j,1,n) ans += a[j] / i + ( a[j] % i > 0 ) - 1;
			res = min(res, ans + i );
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}