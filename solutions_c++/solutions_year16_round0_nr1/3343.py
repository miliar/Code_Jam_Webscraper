#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		int n;
		cin >> n;
		int cnt = 0;
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		bool found[10];
		for (int i = 0; i < 10; i++)
			found[i] = false;
		int cur = n;
		while (true) {
			int tmp = cur;
			while (tmp > 0) {
				if (!found[tmp % 10]) {
					cnt++;
					found[tmp % 10] = true;
				}
				tmp /= 10;
			}
			if (cnt == 10)
				break;
			cur += n;
		}
		cout << cur << endl;
	}
	return 0;
}
