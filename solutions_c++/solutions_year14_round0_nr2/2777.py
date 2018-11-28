#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <numeric>
#include <complex>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef vector<vector<int> > mat;
#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
#define pb push_back
#define mp make_pair
#define INF 1e+9

double solve(double C, double F, double X)
{
	double ans = 0, nowf = 2.0;
	while (1) {
		ans += (C / nowf);
		if ((X - C) / nowf <= X / (nowf + F)) {
			ans += ((X - C) / nowf);
			break;
		} else {
			nowf += F;
		}
	}
	return ans;
}

int main(void)
{
	int T;
	double c, f, x;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %.7lf\n", i, solve(c, f, x));
	}
	return 0;
}