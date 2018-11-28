#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <functional>

using namespace std;

const int MX = 1e4+10;

int n, x;
vector<int> s;
bool out[MX];

int bsearch(int u) {
	int imin = 1, imax = int(s.size()) - 1, imid;
	while (imax - imin > 3) {
		imid = (imin + imax)/2;
		if (s[imid] <= u) imax = imid;
		else imin = imid;
	}
	for (int i = imin; i <= imax; i++) if (s[i] <= u) return i;
	return imax + 1;
}

void solve(int testcase) {
	scanf("%d%d", &n, &x);
	s.clear();
	s.resize(n+1);
	for (int i = 1; i <= n; i++) scanf("%d", &s[i]);
	sort(s.begin()+1, s.end(), greater<int>());
	int j = n, w = 0;
	for (int i = 1; i <= int(s.size())-1; i++) {
		w++;
		int j = bsearch(x-s[i]);
		if (j < int(s.size())) s.erase(s.begin()+j);
	}
	printf("Case #%d: %d\n", testcase, w);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}