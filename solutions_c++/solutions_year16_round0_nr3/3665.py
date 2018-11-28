#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <algorithm>
#include <assert.h>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
const int N = 1e6 + 10;
int z[N];

long long div(string s, int b) {
	long long d = 1;
	long long res = 0;
	for (int i = 0; i < s.length(); i++) {
		res += (s[i] - '0') * 1LL * d;
		d *= b;
	}


	for (int i = 2; i * 1LL * i <= res; i++) {
		if (res % i == 0) {
			return i;
		}
	}
	return -1;
}
vector <int> calc(string s) {
	vector<int> ans;
	for (int i = 2; i <= 10; i++) {
		int d = div(s, i);
		if (d == -1) {
			return vector<int>();
		}
		ans.push_back(d);
	}
	return ans;
}
int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG
	int n = 16;
	int u = 0;
	cout << "Case #1:" << endl;
	for (int i = 0; i < (1 << n); i++) {
		if (((1 << (n - 1)) & i) && (i & 1)){
			string s;
			int x = i;
			while (x > 0) {
				s.push_back('0' + (x % 2));
				x /= 2;
			}
			vector <int> ans = calc(s);
			if (ans.empty()) continue;
			reverse(s.begin(), s.end());
			cout << s << " ";
		
			for (int i = 0; i < ans.size(); i++) {
				cout << ans[i] << " ";
			}
			cout << endl;
			u++;
			if (u == 50) {
				return 0;
			}
		}
	}
	return 0;
}