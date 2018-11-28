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
	//ios::sync_with_stdio(false);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	int cur = 1;
	while (t--) {
		long long n;
		cin >> n;
		if (!n) {
			cout << "Case #" << cur << ": " << "INSOMNIA" << endl;
			cur++;
			continue;
		}
		map<int, int> ls;
		int cnt = 1;
		while ((int)ls.size() != 10) {
			long long temp = cnt * n;
			while (temp > 0) {
				ls[temp % 10]++;
				temp /= 10;
			}
			cnt++;
		}
		cout << "Case #" << cur << ": " << n * (cnt - 1) << endl;
		cur++;
	}
	return 0;
}