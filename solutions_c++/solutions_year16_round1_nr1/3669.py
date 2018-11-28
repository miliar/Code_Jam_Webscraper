#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, caseNum;
	string s;
	cin >> n;
	caseNum = n;
	while (n--) {
		cin >> s;
		string output;
		output.push_back(s[0]);
		if (s.size() == 1) {
			cout << "Case #" << caseNum - n << ": " << s << endl;
			continue;
		}
		for (int i = 1; i < s.size(); i++) {
			if (s[i] >= output[0]) output.insert(output.begin(), s[i]);
			else output.push_back(s[i]);
		}
		cout << "Case #" << caseNum - n << ": " << output << endl;
	}
	return 0;
}