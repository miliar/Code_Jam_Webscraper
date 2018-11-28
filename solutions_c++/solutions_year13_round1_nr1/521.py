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

string fileName = "A-large";

#define ULL unsigned long long

ULL inf = 3000000000000000000LL;

long long getSum(long long n) {
	if (n >= 2000000000) return inf;
	if (n * (n + 1) >= inf * 6 / (2 * n + 1)) return inf;
	return n * (n + 1) * (2 * n + 1) / 6;
}

ULL getSum(unsigned long long r,unsigned long long m) {
	ULL sum = (2 * r + 2 * m - 1);
	if (sum > inf / m) return inf;
	return sum * m;
}

void solveSingle(int testNumber) {
	ULL r, t;
	cin >> r >> t;
	ULL low = 0, up = t;

	printf("Case #%d: ", testNumber);

	while (low < up) {
		ULL mid = (low + up + 1) / 2;
		if (getSum(r, mid) <= t) low = mid;
		else up = mid - 1;
	}

	cout << low << endl;
}

int main() {
//	cout << getSum(3, 5) << endl;
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
