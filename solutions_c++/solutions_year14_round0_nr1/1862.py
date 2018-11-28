/*

jsrkrmciB

*/

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clear(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define Fora(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define fora(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define output(x) cout << (x)
#define ST first
#define ND second
#define br printf("\n")
#define getnum(x) scanf("%d", &x);
#define GCJ(x,y)  printf("Case #%d: %d\n", x+1, y);
#define getline(x) 	scanf("\n%[^\n]",x);

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

const ld PI  = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

#define DEBUG

#ifdef DEBUG
#define debug(x) cout << #x << ":" << x << "\n";
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define debug //
#define dprintf(fmt,...)
#endif

// Global Variable
int N;

int main() {
	freopen("A-small-attempt0.in", "rt", stdin); 
	freopen("A-small-attempt0.out", "wt", stdout); 
	getnum(N);
	fora(T,N){
		int answer=-1;
		int r,t,c[4],d[4];
		getnum(r);
		fora(i,4){
			if(i==r-1){
				getnum(c[0]);
				getnum(c[1]);
				getnum(c[2]);
				getnum(c[3]);
			}else{
				getnum(t);
				getnum(t);
				getnum(t);
				getnum(t);
			}
		}
		getnum(r);
		fora(i,4){
			if(i==r-1){
				getnum(d[0]);
				getnum(d[1]);
				getnum(d[2]);
				getnum(d[3]);
			}else{
				getnum(t);
				getnum(t);
				getnum(t);
				getnum(t);
			}
		}
		fora(i,4){
			fora(j,4){
				if(c[i]==d[j]){
					if(answer==-1)
						answer=c[i];
					else
						answer=-2;
				}
			}
		}
		if(answer==-1)
			printf("Case #%d: Volunteer cheated!\n", T+1);
		else if(answer==-2)
			printf("Case #%d: Bad magician!\n", T+1);
		else
			printf("Case #%d: %d\n", T+1,answer);
	}
	return 0;
}