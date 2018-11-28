#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, c = 1;
	string s;
	scanf("%d", &t);
	while(t--) {
		cin >> s;
		int count = 0, i = 0;
		while(true) {
			bool flag = false;
			while(s[i] == '-' && i < s.size()) {
				flag = true;
				i++;
			}
			if(flag)count++;
			flag = false;
			while(s[i] == '+' && i < s.size()) {
				flag = true;
				i++;
			}
			if(flag && i < s.size())count++;
			if(i >= s.size()) break;
		}
		printf("Case #%d: %d\n", c++, count);
	}
	return 0;
}