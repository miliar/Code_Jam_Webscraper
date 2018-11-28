//#pragma comment(linker, "/STACK:134217728")
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define MOD 1000000009
#define INF 1000000007
#define y1 agaga
#define ll long long
#define ull unsigned long long

long long solve(long long x) {
	int sol = 0;
	int m = 0;
	while (m + 1 != (1 << 10)) {
		++sol;
		long long nx = sol * x;
		while (nx > 0) {
			m |= (1 << (nx % 10));
			nx /= 10;
		}

	}
	return sol*x;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	FOR(T, 0, t) {
		cout << "Case #" << T+1 << ": ";
		int k, c, s;
		cin >> k >> c >> s;
		long long X = 1;
		FOR(i, 0, c - 1)
			X *= k;
		FOR(i, 0, s)
			cout << i*X + 1 << " ";
		cout << endl;
	}

	return 0;
}