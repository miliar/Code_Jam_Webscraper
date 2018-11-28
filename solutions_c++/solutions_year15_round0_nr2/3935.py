// Problem B. Infinite House of Pancakes
#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

int ans = 0;

void doit(map<int, int> &m, int count)
{
	map<int, int>::reverse_iterator it = m.rbegin();
	if (it->first <= 1) {
		ans = min(ans, count + 1);
		return;
	}
	int k = it->first, v = it->second;
	for (int i = 2; i * i <= k; i++) {
		map<int, int> t = m;
		t.erase(k);
		t[k / i] += v * (i - k % i);
		if (k % i) t[k / i + 1] += v * (k % i);
		int c = count + v * (i - 1);
		ans = min(ans, c + t.rbegin()->first);
		doit(t, c);
	}
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d\n", &T);
	for (int ti = 1; ti <= T; ti++) {
		int d, p;
		scanf("%d", &d);
		ans = 0;
		map<int, int> m;
		for (int i = 0; i < d; i++) {
			scanf("%d", &p);
			m[p]++;
			ans = max(ans, p);
		}
		doit(m, 0);
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
