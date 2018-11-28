#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<string>

using namespace std;

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	cin >> t;
	int done = 0;
	while (done<t) {
		string s;
		cin >> s;
		int count = 0;
		for (int i = 1; i < s.size(); i++) {
			if (s[i] != s[i - 1]) count++;
		}
		if (s[s.size() - 1] == '-') count++;
		++done;
		cout << "Case #" << done << ": " << count;
		cout << endl;
	}
	return 0;
}