// @author aliabdallah
// #includes {{{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
#include <utility>
#include <numeric>
#include<list>
#include<iomanip>
#include<cmath>
#include<stack>
#include<complex>
#include<valarray>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define rep1(i,a,b) for(int i=(a);i<=(b);i++)
#define repl(i,x) for(int i=0;x[i];i++)
#define per(i,n) for(int i=(n)-1;i>=0;i--)
#define per1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define dri(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define drii(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define driii(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) cin >> x
#define drs(x) string x; RS(x)
#define pi(x) printf("%d\n",x)
#define pis(x) printf("%d ",x)
#define P(x) cout<<#x<<" = { "<<x<<" }\n"
#define caset int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define mp make_pair
#define pb push_back
#define ms0(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define MSN(x,d) memset(x, d, sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define f first
#define s second
#define NTS(x,y) stringstream ss; ss << x; y = ss.str() //add by theyaserfox, note : '{' & '}' must be add before and after
#define STN(x,y) stringstream ss(x); ss >> y //add by theyaserfox, note : '{' & '}' must be add before and after
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;int main() {
#define FILEIOS ;
#endif
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
const ll OO = 1e8;
const double eps = (1e-7);
// }}}
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)


int main()
{
	READ("A-Small.in");
	WRITE("A-Small.out");
	int counter = 1;
	caset
	{
		dri(n1);
		int arr1[4][4], x, arr2[4][4];
		set<int> s;
		rep(i, 4)
		{
			rep(j, 4)
			{
				cin >> x;
				arr1[i][j] = x;
				if(i==n1-1)
					s.insert(x);
			}
			
		}
		dri(n2);
		rep(i, 4)
		{
			rep(j, 4)
			{
				cin >> x;

				arr2[i][j] = x;
				if(i==n2-1)
					s.insert(x);
			}
			
		}
		cout << "Case #" << counter++ << ": ";
		int size = sz(s);
		if(size == 8)
			cout << "Volunteer cheated!";
		else if(size == 7)
		{
			rep(i, 4)
				rep(j, 4)
					if(arr1[n1-1][i] == arr2[n2-1][j]){
						cout << arr1[n1-1][i];
						break;
					}
		}
		else
			cout << "Bad magician!";
		cout << "\n";
	}

	return 0;
}