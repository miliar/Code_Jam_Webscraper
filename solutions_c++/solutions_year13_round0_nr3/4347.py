#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define int long long

#define ff first
#define ss second
#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 200 + 1;

int a[maxN];
bool ispal (int x) {
	int len = 0;
	for (; x; x /= 10) a[len] = x % 10, len++;
	for (int i = 0, j = len - 1; i < j; i++, j--)
		if (a[i] != a[j]) return false;
	return true;
}

int find (int x) {
	int cnt = 0;
	for (int i = 1; i * i <= x; i++) if (ispal (i) && ispal (i * i)) cerr << i << endl, cnt++;
	return cnt;
}

main() {
	ios::sync_with_stdio (false);
	
	int o; cin >> o;
	for (int i = 0; i < o; i++) {
		int a, b; cin >> a >> b;
		int ans = find (b) - find (a - 1);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}
