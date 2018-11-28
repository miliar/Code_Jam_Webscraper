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
int N,M;

int compare (const void * a, const void * b){
	if(*(const float*)a < *(const float*)b)
        return -1;
  	return *(const float*)a > *(const float*)b;
}

int popLarger (float a, float *b){
	float t;
	fora(i,M){
		if(b[i]==-1) continue;
		if(a<b[i]){
			t=b[i];
			b[i]=-1;
			// printf("(%f)",t);
			return t;
		}
	}
	fora(i,M){
		if(b[i]==-1) continue;
		b[i]=-1;
		return -1;
	}
	printf("ERROR");
	return -2;
}

int war(float *a, float *b){
	int t=0,score=0;
	fora(i,M){
		if(popLarger(a[i],b)==-1){
			score++;
		}
	}
	return score;
}

int main() {
	freopen("D-large.in", "rt", stdin); 
	freopen("D-large.out", "wt", stdout); 
	getnum(N);
	fora(T,N){
		float *a,*b,*c,*d;
		getnum(M);
		a = new float[M];
		b = new float[M];
		c = new float[M];
		d = new float[M];
		fora(i,M)
			scanf("%f",&c[i]);
		fora(i,M)
			scanf("%f",&b[i]);
		qsort (c, M, sizeof(float), compare);
		qsort (b, M, sizeof(float), compare);
		fora(i,M)
			a[i]=c[M-i-1];
		fora(i,M)
			d[i]=b[M-i-1];
		printf("Case #%d: ", T+1);
		printf("%d %d",M-war(d,c),war(a,b));
		printf("\n");
	}
	return 0;
}