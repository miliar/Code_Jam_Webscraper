#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define  _SCL_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define REP(a,b) for(long long a = 0;a < b;++a)
int main() {
	int t;
	cin >> t;
	for (int i = 0;i < t;++i) {
		int n;
		cin >> n;
		map<int, int> counter;
		vector<int> on;
		for (int j = 0;j < n * 2 - 1;++j) {
			for (int k = 0;k < n;++k) {
				int a;
				cin >> a;
				counter[a]++;
			}
		}
		vector<int> ans;
		for (auto itr = counter.begin(); itr != counter.end(); ++itr) {
			int hogehoge = itr->second;
			if (hogehoge % 2 == 1) {
				ans.push_back(itr->first);
			}
		}
		sort(begin(ans), end(ans));
		cout << "Case #" << i + 1 << ":";
		for (int j = 0;j < ans.size();++j) {
			cout << " " << ans[j];
		}
		cout << endl;
	}
}