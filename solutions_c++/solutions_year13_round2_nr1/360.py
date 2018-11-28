#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
#include <cstdarg>
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
void print(const char *fmt, ...)  { va_list args; va_start(args, fmt); vprintf(fmt, args); vfprintf(stderr, fmt, args); va_end(args); }

#define MAXN 101
#define MAXK 1000111

int m[MAXN][MAXK];
int a[MAXN];

int N, M, K;

int solve(int p, int k)
{
	int& r = m[p][k];
	if (r != -1)
		return r;

	if (p==N)
		return 0;
	r = 1 + solve(p+1, k); // skip

	if (k == 1 && k <= a[p])
		return r;

	int t=0;
	while (k <= a[p])
	{
		k += k-1;
		t += 1;
	}
	t += solve(p+1, min(MAXK-1, k+a[p]));
	r = min(r, t);
	return r;
}

int main()
{
	freopen("inA.txt", "r", stdin);
	freopen("outA.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		print("Case #%d: ", Case+1);

		fill(m,-1);

		scanf("%d%d", &K, &N);
		FOR(i,0,N) scanf("%d", &a[i]);
		sort(a, a+N);

		int res = solve(0, K);
		print("%d\n", res);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
