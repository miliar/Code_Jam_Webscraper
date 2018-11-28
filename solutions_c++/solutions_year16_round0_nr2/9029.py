#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <assert.h>

using namespace std;
typedef long long int LLI;

string g(string s, int pos) {
	assert(pos <= s.size());
	string result = s;
	reverse(result.begin(), result.begin() + pos);
	for (int i = 0; i < pos; i++) {
		if (result[i] == '-') result[i] = '+';
		else result[i] = '-';
	}
	return result;
}
int f(string s) {
	string canon;
	canon.resize(s.size());
	for (int i = 0; i < canon.size(); i++) {
		canon[i] = '+';
	}
	if (s == canon) return 0;
	queue<string> q;
	map<string, int> color;
	q.push(s);
	color[s] = 0;
	while (!q.empty()) {
		string str = q.front();
		q.pop();
		for (int i = 0; i < str.size(); i++) {
			string result = g(str, i+1);
			if (color.count(result) == 0) {
				q.push(result);
				color[result] = color[str] + 1;
				if (result == canon) return color[result];
			}
		}
	}
}
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	string s;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> s;
		LLI result = f(s);
		cout << "Case #" << (i + 1) << ": " << result << endl;
	}
	return 0;
}