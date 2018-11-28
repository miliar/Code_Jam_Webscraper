#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include<functional>
#include <fstream>
#define ii pair<int,int>
#define INF 1000000000
using namespace std;
int main()
{
	freopen("outputB.txt","w",stdout);
	int t, l;
	cin >> t;
	for (l = 0; l < t; l++) {
		map <int, int> mp;
		int n;
		cin >> n;
		for (int i = 0; i < 2 * n - 1; i++) {
			for (int j = 0; j < n; j++) {
				int x;
				cin >> x;
				mp[x]++;
			}
		}
		vector <int> ans;
		for (std::map<int, int>::iterator it = mp.begin(); it != mp.end(); ++it) {
			if (it->second % 2 != 0)
				ans.push_back(it->first);
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << l + 1 << ": ";
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i] << ' ';
		cout << endl;
		mp.clear();
		ans.clear();
	}
	return 0;
}
