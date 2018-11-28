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
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 2007;
int N, A[MAX], B[MAX], res[MAX], AA[MAX], BB[MAX], orig[MAX], temp[MAX];

void calc(int nums[MAX], int A[MAX], int B[MAX])
{
	FOR(i, 0, N-1)
	{
		A[i] = 1;
		FOR(j, 0, i-1)
			if (nums[i] > nums[j])
				chmax(A[i], A[j]+1);
	}
	FORD(i, N-1, 0)
	{
		B[i] = 1;
		FORD(j, N-1, i+1)
			if (nums[i] > nums[j])
				chmax(B[i], B[j]+1);
	}
}

void check()
{
	REP(i, N)
		if (!res[i])
			DEBUG("AAAAAAAAAAAAAAAAA")
	calc(res, AA, BB);
	REP(i, N)
		if (AA[i] != A[i] || BB[i] != B[i])
			DEBUG("BBBBBBBBBBBBBBBBBBBBBB");
}

void Solve(int tc)
{
	cin >> N;
	REP(i, N) cin >> A[i];
	REP(i, N) cin >> B[i];
	/*N = rand() % 2000 + 1;
	REP(i, N) orig[i] = i+1;
	random_shuffle(orig, orig+N);
	calc(orig, A, B);*/

	memset(res, 0, sizeof(res));
	REP(i, N) AA[i] = BB[i] = 1;
	FOR(n, 1, N)
	{
		FORD(i, N-1, 0)
		{
			temp[i] = (i==N-1?INF:temp[i+1]);
			if (!res[i] && AA[i] == A[i])
				chmin(temp[i], A[i]);
		}
		int x = INF;
		FOR(i, 0, N-1)
		{
			if (res[i]) continue;
			if (A[i] == AA[i] && B[i] == BB[i] && x > B[i] && (i==N-1 || temp[i+1] > A[i]))
			{
				res[i] = n;
				FOR(j, 0, i-1) chmax(BB[j], B[i]+1);
				FOR(j, i+1, N-1) chmax(AA[j], A[i]+1);
				break;
			}
			if (B[i] == BB[i])
				chmin(x, B[i]);
		}
	}

	check();

	printf("Case #%d:", tc);
	REP(i, N) printf(" %d", res[i]);
	printf("\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}