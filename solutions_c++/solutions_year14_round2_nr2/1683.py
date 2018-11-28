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

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int a, b, k;
		cin >> a >> b >> k;
		int ans = 0;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if ((i & j) < k)
					ans++;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}