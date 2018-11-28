#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <omp.h>
#include <windows.h>

using namespace std;

#define FOR(i, s, t) for(int i(s); i<=(int)(t); i++)
#define REP(i, n) FOR(i,0,n-1)
#define ALL(a) a.begin(),a.end()

vector<string> ansstr;

void update(double &x, double y) {
	if (y > x) x = y;
}

const int N = 202;
double a[N];
int c[N];
int n, K;

double run(vector<double> a, int k) {
	double dis[2][N * 2];
	int x = 0, y = 1;
	memset(dis, 0, sizeof(dis));
	dis[x][0] = 1.0;
	REP(i, a.size()) {
		double p = a[i];
		memset(dis[y], 0, sizeof(dis[y]));
		REP(j, i + 1) {
			dis[y][j] += dis[x][j] * (1 - p);
			dis[y][j + 1] += dis[x][j] * p;
		}
		swap(x, y);
	}
	return dis[x][k];
}

void Work(int casen) {
	cin >> n >> K;
	REP(i, n) cin >> a[i];
	sort(a, a + n);
	double ans = 0;
	REP(o, K + 1) {
		vector<double> tmp;
		REP(i, o) tmp.push_back(a[i]);
		REP(i, K - o) tmp.push_back(a[n - 1 - i]);
		ans = max(ans, run(tmp, K / 2));
	}
	ostringstream oss;
	oss << "Case #" << casen << ": ";
	oss << ans;
	oss << endl;
	ansstr[casen - 1] = oss.str();
}

int main() {
	// omp_set_num_threads(4);

	int n;
	cin >> n;
	ansstr.resize(n);

	//#pragma omp parallel for schedule(dynamic)
	for (int i = 1; i <= n; i++) Work(i);

	for (int i = 0; i < n; i++) cout << ansstr[i];

	return 0;
}
