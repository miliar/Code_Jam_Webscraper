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
int qq;

int findmax(int P[1001]){
	int maxp;
	fora(p,1001){
		if(P[p]) {
			maxp=p;
		}
	}
	return maxp;
}
int findmax2(int P[1001], int t){
	int maxp2=0;
	int maxp=findmax(P);
	fora(p,1001){
		if(p==maxp) break;
		if(P[p]||p==t) {
			maxp2=p;
		}
	}
	return maxp2;
}
void printP(int P[1001],int ans){
	fora(p,10){
		if(p==0) continue;
		printf("%d ",P[p]);
	}
	printf("ans=%d\n",ans);
}
int main() {
	freopen("B.in", "rt", stdin); 
	freopen("B.out", "wt", stdout); 
	getnum(qq);
	fora(T,qq){
		int ans=0;
		int S=0;
		int D;
		int P[1001],p,t=10000;
		fora(i,1001) P[i]=0;
		getnum(D);
		fora(d,D){
			getnum(p);
			P[p]++;
			S+=p;
		}
		p=findmax(P);
		for(int i=1;i<=p;i++){
			int tt = 0;
			int SS = S;
			for(int pp=1;pp<=p;pp++){
				if(pp>i){
					tt+=((pp-1)/i)*P[pp];
				}
			}			
			t=min(t,tt+i);
			
		}

		// 5 5 5 9 9 9
		// 9
		// 0 - 


		// 	printf("1 2 3 4 5 6 7 8 9\n");

		// while(1){
		// 	printP(P,ans);
		// 	p = findmax(P);
		// 	int t=0;
		// 	int ti=1;
		// 	for(int i=2;i<=p;i++){
		// 		int tt = p-i*(p/i)+(p/i); //broke
		// 		int p2 = findmax2(P,tt);
		// 		t = max(t,p-p2-P[p]*(i-1));
		// 		if(t==p-p2-P[p]*(i-1)) ti=i;
		// 	}
		// 	if(ti<2) break;
		// 	P[p/ti]+=P[p]*(ti-1);
		// 	P[p-ti*(p/ti)+(p/ti)]+=P[p];
		// 	ans+=P[p]*(ti-1);
		// 	P[p]=0;
		// }

		printf("Case #%d: %d\n", T+1, t);
	}
	return 0;
}