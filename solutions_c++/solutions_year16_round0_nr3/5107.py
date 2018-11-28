#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

static int isDivisible(__int64 x)
{
	__int64 limit = sqrt(1.0*x);
	limit = min(limit, x - 1);
	for (int i = 2; i <= limit; i++) {
		if (x % i == 0) return i;
	}
	return -1;
}

int main()
{
	const int N = 16, J = 50;
	map<int,vector<int>> ans;
	for (int i = (1 << (N - 1)) + 1; i < (1 << N); i += 2) {
		for (int b = 2; b <= 10; b++) {
			__int64 n = 0, p = 1, t = i;
			while(t) {
				if (t & 1) n += p;
				t >>= 1;
				p *= b;
			}
			if (auto d = isDivisible(n)) {
				if (d < 0) break;
				ans[i].push_back(d);
			}
		}
		if (ans[i].size() < 9) ans.erase(i);
		if (ans.size() == J) break;
	}

	cout << "Case #1:" << endl;
	for (auto& p : ans) {
		int x = p.first;
		string s;
		while (x) {
			s.append(x & 1 ? "1" : "0");
			x >>= 1;
		}
		reverse(s.begin(), s.end());
		cout << s;
		for (auto& v : p.second) {
			cout << " " << v;
		}
		cout << endl;
	}

	return 0;
}
