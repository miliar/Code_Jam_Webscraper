#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair

const int N = 105;
int n;
double V, X, R[N], C[N];

void solve() {
	static int caseCnt = 0;
	printf("Case #%d: ", ++caseCnt);
	cin >> n >> V >> X;
	double RR = 0;
	vector<pair<double, double> > A, B;
	REP(i, n) {
		cin >> R[i] >> C[i];
		if (fabs(C[i] - X) < 1e-9)
			RR += R[i];
		else if (C[i] < X)
			A.push_back(make_pair(C[i], R[i]));
		else
			B.push_back(make_pair(C[i], R[i]));
	}
	sort(ALL(A));
	reverse(ALL(A));
	sort(ALL(B));
	int i = 0, j = 0;
	while (i < (int)A.size() && j < (int)B.size()) {
		double r = (A[i].first - X) / (X - B[j].first);
		if (A[i].second < B[j].second / r) {
			RR += A[i].second * (1 + r);
			B[j].second -= A[i].second * r;
			i++;
		} else {
			RR += B[j].second * (1 + 1.0 / r);
			A[i].second -= B[j].second / r;
			j++;
		}
	}
	if (fabs(RR) < 1e-9) {
		puts("IMPOSSIBLE");
		return ;
	}
	printf("%.10f\n", V / RR);
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

