#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

int main()
{
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		string S;
		cin >> S;

		vector<char> ans;
		for (auto i : S) {
			if (ans.empty()) {
				ans.push_back(i);
			} else {
				int j;
				for (j = 0; j < ans.size(); ++j) {
					if (ans[j] < i) {
						ans.insert(ans.begin(), i);
						break;
					} else if (ans[j] > i) {
						ans.push_back(i);
						break;
					}
				}
				if (j == ans.size())
					ans.push_back(i);
			}
		}
		cout << "Case #" << tc << ": ";
		for (auto i : ans) {
			cout << i;
		}
		cout << endl;
	}
}
