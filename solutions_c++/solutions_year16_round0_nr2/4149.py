#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
	freopen("test.txt", "r", stdin);
	freopen("test.out.txt", "w", stdout);

	int t;
	cin>>t;
	for (int cas = 1; cas <= t; cas++) {
		string s;
		cin>>s;
		int cur = s[0] == '-';
		int num = cur;
		int cnt = 0;
		for (int i=1;i<s.size();i++) {
			if (s[i] == '-' && cur == 1) continue;
			if (s[i] == '+' && cur == 0) continue;
			cur = 1 - cur;
			if (s[i] == '-')
				cnt++;
		}
		cout << "Case #" << cas << ": " << cnt * 2 + num << endl;
	}
	return 0;
}