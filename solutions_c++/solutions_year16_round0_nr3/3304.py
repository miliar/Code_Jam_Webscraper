#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

string gen(int n, int i, int j, int k, int l) {
	int m = (n - 2) / 2;
	vector<int> a(m), b(m);
	a[i] = a[j] = b[k] = b[l] = 1;
	string res;
	res.push_back('1');
	for (int x = 0; x < m; ++x) {
		res.push_back('0' + a[x]);
		res.push_back('0' + b[x]);
	}
	res.push_back('1');
	return res;
}

vector<string> gen(int n, int x) {
	vector<string> res;
	int m = (n - 2) / 2;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < i; ++j) {
			for (int k = 0; k < m; ++k) {
				for (int l = 0; l < k; ++l) {
					res.push_back(gen(n, i, j, k, l));
					if (res.size() >= x) return res;
				}
			}

		}
	}

	return res;
}

void solve() {
	int n, j;
	cin >> n >> j;
	auto vs = gen(n, j);
	for (auto s : vs) {
		cout << s;
		for (int i = 3; i <= 11; ++i) {
			cout << ' ' << i;
		}
		cout << endl;
	}
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ":" << endl;
		solve();
	}

}