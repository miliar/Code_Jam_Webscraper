#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <stack>
#include <map>
#include <numeric>
using namespace std;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define out(x) cout << (x) << endl;
#define fill(a, x) memset(a, x, sizeof(a))
#define all(c) c.begin(), c.end()
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
const int INF = (long long) 1e9;
const double EPS = 1e-9;

int main() {
	int n;
	cin >> n;
	for(int i = 0; i < n; i++) {
		double rate = 2.0, extra, cost, target;
		cin >> cost >> extra >> target;
		double best = target / 2.0, elapsed = 0.0;
		double best0 = best;
		for(int i = 1; i <= 1e6; i++) {
			elapsed += cost / rate;
			if (elapsed > best0 + EPS) break;
			rate += extra;
			best = min(best, elapsed + target / rate);
		}
		printf("Case #%d: %.7lf\n", i+1, best);
	}
	return 0;
}