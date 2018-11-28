#include <bits/stdc++.h>
using namespace std;

multiset<int> ms;
int arr[1005];

bool chk (multiset<int> c) {
	return c.count(4) > 0 || c.count(5) > 0
			|| c.count(7) > 0 || c.count(8) > 0;
}

int solve (multiset<int> c) {
	multiset <int> tmp = c;
	multiset <int> :: iterator it = tmp.end();
	it --;
	int cur = *it;
	if (cur == 1) {
		return cur;
	}
	int ret = cur;
	tmp.erase(it);
	if (cur == 9) {
		tmp.insert(3);
		tmp.insert(6);
		ret = min(ret, 1+solve(tmp));
		tmp.erase(tmp.find(3));
		tmp.erase(tmp.find(6));
		tmp.insert(4);
		tmp.insert(5);
		ret = min(ret, 1+solve(tmp));
	}
	else {
		int rem = cur / 2;
		tmp.insert(cur - rem);
		tmp.insert(rem);
		ret = min(ret, 1+solve(tmp));
	}
	return ret;
}

int main() {
	//freopen("input.in","r",stdin);
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	int kase = 1;
	cin >> t;
	while (t --) {
		ms.clear();
		int n;
		cin >> n;
		for (int i=0; i<n; i++) {
			cin >> arr[i];
			ms.insert(arr[i]);
		}
		int ret = solve (ms);
		cout << "Case #" << kase++ << ": " << ret << endl;
	}
	return 0;
}
