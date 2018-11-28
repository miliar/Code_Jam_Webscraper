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
	int t, tn=1;
	scanf("%d", &t);
	while(t--) {
		int r1, r2;
		vi a,b;
		scanf("%d", &r1);
		rep(i,4) {
			rep(j,4) {
				int k;
				scanf("%d", &k);
				if(i == r1-1) a.pb(k);
			}
		}
		scanf("%d", &r1);
		rep(i,4) {
			rep(j,4) {
				int k;
				scanf("%d", &k);
				if(i == r1-1) b.pb(k);
			}
		}
		r1 = 0;
		rep(i,4) rep(j,4) if(a[i] == b[j]) r1++, r2 = a[i];
		printf("Case #%d: ", tn++);
		if(r1 == 1) printf("%d", r2);
		else printf("%s",r1==0?"Volunteer cheated!":"Bad magician!");
		pn;
	}
}