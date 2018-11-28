#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>

// using namespace __gnu_pbds;
using namespace std;

#pragma comment(linker, "/STACK:16777216")

#define Foreach(i, c) \
  for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i, a, b) for (int(i) = (a); (i) < (b); ++(i))
#define rof(i, a, b) for (int(i) = (a); (i) > (b); --(i))
#define rep(i, c) for (auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define PB pop_back()
#define iOS ios_base::sync_with_stdio(false)
#define sqr(a) (((a) * (a)))
#define pow2(a) (((a) * (a)))
#define all(a) a.begin(), a.end()
#define error(x) cerr << #x << " = " << (x) << endl
#define Error(a, b)                                                     \
  cerr << "( " << #a << " , " << #b << " ) = ( " << (a) << " , " << (b) \
       << " )\n";
#define errop(a) cerr << #a << " = ( " << ((a).x) << " , " << ((a).y) << " )\n";
#define coud(a, b) cout << fixed << setprecision((b)) << (a)
#define L(x) (((x) << 1) + 1)
#define R(x) (((x) << 1) + 2)
#define umap unordered_map
//#define double long double
#define mod 1000000007
#define mod1 1000000009
#define LIMIT 10000000000000000LL
#define MAX1 1000000000
//#define si(n) scanf("%d",&n)
//#define sii(n,m) scanf("%d%d",&n,&m)
//#define pi(n) printf("%d\n",n)
const int inf = 0x3f3f3f3f;
const long double pi = acos(-1.0);
#define INF 1000000000000000000LL
#define MAX 1000005
#define N 410
const string debug_line = "yolo";
#define debug error(debug_line)
const double PI = 4 * atan(1);
#define read() freopen("mergedoutput.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
// template <typename T> using os =  tree<T, null_type, less<T>, rb_tree_tag,
// tree_order_statistics_node_update>;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef complex<double> point;

ll dp[1000001];

void calc(){
	For(i,1,1000001){
		// error(i);
		set<int> s1;
		int j=1;
		while(true){
			ll num=(ll)i*(ll)j;
			while(num!=0){
				s1.insert(num%10);
				num=num/10;
			}
			if(s1.size()==10){
				break;
			}
			else{
				j++;
			}
		}
		dp[i]=j;
	}
}

int main(){
	calc();

	For(i,1,201){
		Error(i,dp[i]);
	}

	int t;
	scanf("%d",&t);
	For(t1,1,t+1){
		int n;
		scanf("%d",&n);
		ll answer1=n*dp[n];
		printf("Case #%d: ",t1);
		if(n==0){
			printf("INSOMNIA\n");
		}
		else{
			printf("%lld\n",answer1);
		}
	}
}