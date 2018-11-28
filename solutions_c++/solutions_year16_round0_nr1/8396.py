#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std; 
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }

/////////////////////////////////////////////////////////////////////

int GetMask(int number) {
	int mask = 0;
	while(number) {
		mask |= (1 << (number%10));
		number /= 10;
	}

	return mask;
}

int MXN = 1000000;
int Ans[2000000];
int main()
{
	int TargetMask = 0;
	for(int i = 0; i < 10; ++i) TargetMask |= (1 << i);
	Ans[0] = -1;
	for(int i = 1; i <= MXN; ++i) {
		int mask = GetMask(i);
		int N = i;
		while(mask != TargetMask) {
			N += i;
			mask |= GetMask(N);
		}
		Ans[i] = N;
	}

	int T;
	scanf("%d", &T);

	int t = 1;
	while(T--) {
		int N;
		scanf("%d", &N);
		if(N == 0)
			printf("Case #%d: INSOMNIA\n", t++);
		else
			printf("Case #%d: %d\n", t++, Ans[N]);
	}

    return 0;
}  

