#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <deque>
#include <functional>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	int num = 1;
	while (T--) {
		int n;
		cin >> n;
		vector<pair<int, char> > s;
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			s.push_back({ x, 'A' + i });
		}
		sort(s.begin(), s.end());
		cout << "Case #" << num << ": ";
		while (true) {
			if ((int)s.size() == 2) {
				while (s[0].first) {
					cout << s[0].second << s[1].second << " ";
					s[0].first--;
					s[1].first--;
				}
				break;
			}
			else {
				cout << s.back().second << " ";
				s.back().first--;
				vector<pair<int, char> > temp;
				for (int i = 0; i < (int)s.size(); i++)
					if (s[i].first)
						temp.push_back(s[i]);
				s = temp;
				sort(s.begin(), s.end());
			}
		}
		cout << endl;
		num++;
	}
	return 0;
}