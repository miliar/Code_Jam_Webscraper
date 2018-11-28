#pragma comment(linker,"/STACK:256000000")
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef long long ull;
const ull mod = 1000000000000000007;

int solve(int test) {
	string s;
	int smax, cnt = 0,ans = 0;
	cin >> smax;
	cin >> s;
	for (int i = 0; i < int(s.size()); i++) {
		if (cnt < i) {
			int val = i - cnt;
			ans += val;
			cnt += val;
		}
		cnt += int(s[i] - '0');
	}
	std::cout << "Case #"<< test <<": " << ans << '\n';
	return 0;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	//cin.ignore();
	for (int tt = 0; tt < T; tt++) {
		solve(tt+1);
	}
}
