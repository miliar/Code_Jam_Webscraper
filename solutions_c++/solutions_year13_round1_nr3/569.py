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

string fileName = "C-small-1-attempt3";
//string fileName = "C-sample";

void solveSingle(int testNumber) {
	srand(time(NULL));
	int r, n, m, k;
	cin >> r >> n >> m >> k;

	printf("Case #1:\n");

	vector<int> p;
	p.resize(7);
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < k; j++)
			cin >> p[j];

		int rx = 2, ry = 2, rz = 2;
		double best = 0.0;

		int num[3];

		for (num[0] = 2; num[0] <= m; num[0]++)
		for (num[1] = 2; num[1] <= m; num[1]++)
		for (num[2] = 2; num[2] <= m; num[2]++) {
			double chance = 1.0;
			for (int a = 0; a < k; a++) {
				double prob = 0.0;
				for (int mask = 0; mask < 1 << n; mask++) {
					int product = 1;
					for (int b = 0; b < k; b++)
						if (mask & 1 << b) product *= num[b];
					if (product == p[a]) {
						prob += 1.0 / (1 << n);
					}
				}
				chance *= prob;
			}
			if (chance > best) {
				best = chance;
				rx = num[0];
				ry = num[1];
				rz = num[2];
			}
		}
		printf("%d%d%d\n", rx, ry, rz);
	}
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
