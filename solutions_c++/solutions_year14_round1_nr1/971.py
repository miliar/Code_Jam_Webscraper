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

int main() {
	int t; gi(t);
	rep(T,t) {
		int n,l;
		scanf("%d%d", &n, &l);
		vector <string> a;
		vector <string> b;
		char s[20];
		rep(i, n) {
			scanf("%s", s);
			a.pb(string(s));
		}
		sort(all(a));
		rep(i,n) {
			scanf("%s", s);
			b.pb(string(s));
		}
		int ans = -1;
		rep(i, 1<<l) {
			vector <string> temp = b;
			rep(j, l) if(i & (1<<j)) {
				rep(k, temp.sz) temp[k][j] = (temp[k][j]=='1'?'0':'1');
			}
			sort(all(temp));
			if(temp == a) {
				// printf("%d %d\n", i, __builtin_popcount(i));
				// rep(i, temp.sz) printf("%s ", temp[i].c_str()); pn;
				if(ans == -1) ans = __builtin_popcount(i);
				else ans = min(ans, __builtin_popcount(i));
			}
		}
		printf("Case #%d: ",T+1);
		if(ans == -1) printf("NOT POSSIBLE\n");
		else printf("%d\n", ans);
	}
}