#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <cassert>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)
#define ALL(a) a.begin(), a.end()
#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define SQR(a) ((a) * (a))

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;
typedef pair<int, int> pii ;
typedef vector<int> vint;
typedef vector<LL> vLL;

const LL nmax = 10000000;
char s[100];
int len;

inline bool ispalin(LL n) {
	sprintf(s, "%I64d", n);
	len = strlen(s);
	for (int i = 0; i < (len >> 1); ++i)
		if (s[i] != s[len - 1 - i])
			return false;
	return true;
}

const int N = 39;
const LL r[N] = {
1, 
4, 
9, 
121, 
484, 
10201, 
12321, 
14641, 
40804, 
44944, 
1002001, 
1234321, 
4008004, 
100020001, 
102030201, 
104060401, 
121242121, 
123454321, 
125686521, 
400080004, 
404090404, 
10000200001, 
10221412201, 
12102420121, 
12345654321, 
40000800004, 
1000002000001LL, 
1002003002001LL, 
1004006004001LL, 
1020304030201LL, 
1022325232201LL, 
1024348434201LL, 
1210024200121LL, 
1212225222121LL, 
1214428244121LL, 
1232346432321LL, 
1234567654321LL, 
4000008000004LL, 
4004009004004LL
};


int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif
	/*for (LL i = 1; i <= nmax; ++i) {
		if (ispalin(i) && ispalin(i * i))
			cout << i * i  << ", " << endl;
	}*/
	int T;
	cin >> T;
	FOR(I, 1, T) {
		LL A, B;
		cin >> A >> B;
		int ans = 0;
		for (int i = 0; i < N; ++i) 
			ans += A <= r[i] && r[i] <= B;
		cout << "Case #" << I << ": " << ans << endl;
	}
	return 0;
}

