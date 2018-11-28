#include <iostream>
#include <fstream>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int A, list[105], posa, n;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int l = 1; l <= t; l++) {	
		cin >> A >> n;
		for (int i = 0; i < n; i++) cin >> list[i];
		list[n] = A;
		int head = 0;
		while (true) {
			sort(list, list + n + 1);
			int sum = 0;
			for (int i = head; i <= n; i++) {
				if (list[i] == A) {
					posa = i;
					break;
				}
				sum += list[i];
			}
			A += sum;
			list[posa] = A;
			head = posa;
			if (sum == 0) break;
		}
		if (posa == n) {
			cout << "Case #" << l << ": 0\n";
			continue;
		} 
		int dis[105], value[105];
		memset(value, -1, sizeof(value));
		memset(dis, 0, sizeof(dis));
		int tmp = list[posa], tmp2 = 0;
		while (true) {
			tmp = tmp * 2 - 1;
			tmp2++;
			if (tmp2 > 100) {
				cout << "Case #" << l << ": " << n - posa << "\n";
				break;
			}
			if (tmp > list[posa + 1]) break;
		}
		if (tmp2 > 100) continue;
		dis[posa + 1] = tmp2;
		value[posa + 1] = tmp + list[posa + 1];
		for (int i = posa + 2; i <= n; i++) {
			if (value[i - 1] > list[i]) {
				value[i] = value[i - 1] + list[i];
				dis[i] = dis[i - 1];
				continue;
			}
			tmp = value[i - 1], tmp2 = dis[i - 1];
			while (true) {
				tmp = tmp * 2 - 1;
				tmp2++;
				if (tmp2 > 100) {
					int ans = n - posa;
					for (int j = posa + 1; j < i; j++) {
						if (dis[j] + n - j < ans) ans = min(ans, dis[j] + n - j);
					}
					cout << "Case #" << l << ": " << ans << "\n";
					break;
				}
				if (tmp > list[i]) break;
			}
			if (tmp2 > 100) break;
			dis[i] = tmp2;
			value[i] = tmp + list[i]; 
		}
		if (tmp2 > 100) continue;
		int ans = n - posa;
		for (int i = posa + 1; i <= n; i++) {
			if (dis[i] + n - i < ans) ans = min(ans, dis[i] + n - i);
		}
		cout << "Case #" << l << ": " << ans << "\n";
	}
	return 0;
}

