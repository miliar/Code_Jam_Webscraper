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
	//freopen("a.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		string s;
		cin >> s;
		int end = s.length() - 1;
		for (; end >= 0; end--) {
			if (s[end] == '-')
				break;
		}
		if (end < 0) {
			cout << 0 << endl;
			continue;
		}
		int cnt = 0;
		for (int i = 0; i < end; i++) {
			if (s[i] != s[i + 1])
				cnt++;
		}
		cout << cnt + 1 << endl;
	}
	return 0;
}
