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
typedef unsigned long long int LLI;

string f(string s) {
	string res;
	res.push_back(s[0]);
	for (int i = 1; i < s.size(); i++) {
		if (s[i] < res[0]) res.push_back(s[i]);
		else{
			res.insert(res.begin(), s[i]);
		}
	}
	return res;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		string s;
		cin >> s;
		cout << "Case #" << (i + 1) << ": " << f(s) << endl;
	}
	return 0;
}