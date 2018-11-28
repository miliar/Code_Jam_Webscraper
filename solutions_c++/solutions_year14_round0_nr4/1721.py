//Template

// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
using namespace std;

//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

#define gi(n) scanf("%d",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
#define dg(n,s); printf("%s %d",s,n)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()

int solve(vector <double> &a, vector <double> &b) {
	int ans = 0, j = b.sz-1;
	rep(i, a.sz) {
		if(a[i] > b[j]) {
			ans++;
		} else j--;
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int T=1; T<=t; T++) {
		int n;
		scanf("%d", &n);
		vector <double> a(n),b(n);
		rep(i,n) scanf("%lf", &a[i]);
		rep(i,n) scanf("%lf", &b[i]);
		sort(all(a));
		reverse(all(a));
		sort(all(b));
		int normal = solve(a,b), best = normal;
		// rep(i,n) {
		// 	a.resize(a.sz-1);
		// 	b.resize(b.sz-1);
		// 	best = max(best, solve(a,b));
		// }
		// // rep(i, n) printf("%.4lf ", a[i]); pn;
		// rep(i, n) printf("%.4lf ", b[i]); pn;
		best = 0; int j = 0;
		reverse(all(a));
		rep(i, a.sz) {
			if(a[i] > b[j]) {
				best++;
				j++;
			}
		}
		printf("Case #%d: %d %d\n", T, best, normal);
	}
}