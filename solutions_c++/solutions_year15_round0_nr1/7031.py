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
#define out(x) cout << (x) << endl
#define fill(a, x) memset(a, x, sizeof(a))
#define all(c) c.begin(), c.end()
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
const int INF = (long long) 1e9;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int n;
		string s;
		cin >> n >> s;
		int sum = s[0]-'0';
		int cost = 0;
		for(int i = 1; i <= n; i++) {
			int dig = s[i] - '0';
			int addcost = max(0, i - sum);
			cost += addcost;
			sum += dig + addcost;
		}
		printf("Case #%d: %d\n", t, cost);
	}
}