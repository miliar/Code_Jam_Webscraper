#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

string fileName = "B-large";

int n;

long long calcbest(long long k) {
	long long t = (1LL << n);
	if (k == t - 1) return t;

	int x = -1;

	for (int i = 1; i <= n; i++)
		if (t - k >= (1LL << i)) x = i;
	return (1LL << (n - x));
}

long long calcworst(long long k) {
	if (k == 0) return 1;
	long long t = (1LL << n);

	int x = -1;

	for (int i = 1; i <= n; i++)
		if (k + 1 >= (1LL << i)) x = i;
	return t - (1LL << (n - x)) + 1;
}

void solveSingle(int testNumber) {
	long long p;
	cin >> n >> p;


	long long x, y;

	long long low = 0, up = (1LL << n) - 1;
	while (low < up) {
		long long mid = (low + up + 1) / 2;
		if (calcworst(mid) <= p) low = mid;
		else up = mid - 1;
	}
	x = low;

	low = 0, up = (1LL << n) - 1;
	while (low < up) {
		long long mid = (low + up + 1) / 2;
		if (calcbest(mid) <= p) low = mid;
		else up = mid - 1;
	}
	y = low;

	printf("Case #%d: %I64d %I64d\n", testNumber, x, y);
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
		fflush(stdout);
	}
	return 0;
}
