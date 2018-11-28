#include "bits/stdc++.h"
using namespace std;
string str;
deque<char> dq;
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.text", "w", stdout);
	int Case;
	cin >> Case;
	for (int tc = 1; tc <= Case; tc++) {
		cin >> str;
		dq.clear();
		int len = str.length();
		for (int i = 0; i < len; i++) {
			if (dq.empty())
				dq.push_back(str[i]);
			else if (dq.front() <= str[i])
				dq.push_front(str[i]);
			else
				dq.push_back(str[i]);
		}
		printf("Case #%d: ", tc);
		for (int i = 0; i < dq.size(); i++)
			printf("%c", dq[i]);
		printf("\n");
	}
	return 0;
}