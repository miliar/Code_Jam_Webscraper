#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

#define NN 1010

int t, N;
char W[NN];
deque<char> ans;

int main() {
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%s", W);
		ans.clear();
		for (char* p = W; *p != '\0'; ++p) {
			char c = *p;
			if (!ans.empty() && c >= ans.front()) {
				ans.push_front(c);
			} else {
				ans.push_back(c);
			}
		}
		ans.push_back('\0');
		string s(ans.begin(), ans.end());
		printf("Case #%d: %s\n", ti+1, s.data());
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
