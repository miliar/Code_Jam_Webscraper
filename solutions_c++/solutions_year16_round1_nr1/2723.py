#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>
#define _USE_MATH_DEFINES
#define vi vector<int>
using namespace std;
int main () {
	freopen ("D:\\Internet\\A-large.in", "r", stdin);
	freopen ("A-large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		string a = "";
		for (int i = 0; i < s.length(); i++) {
			char c = s[i];
			if (i == 0 || c < a[0])
				a = a + c;
			else
				a = c + a;
		}
		cout << "Case #" << t << ": "<< a << endl;
	}
}