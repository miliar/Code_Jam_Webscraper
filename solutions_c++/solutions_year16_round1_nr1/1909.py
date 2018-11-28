#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <fstream>
using namespace std;

int main() {
	freopen ("A-large (1).in", "r",stdin);
	freopen ("output.txt","w",stdout);
	int test,t;
	cin >> t;
	for (test = 1; test <= t; test++) {
		int maxi = -10000;
		string s1="";
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] >= maxi) {
				s1 = s[i] + s1;
				maxi = s[i];
			}
			else {
				s1 = s1 + s[i];
			}
		}
		cout << "Case #" << test << ": " << s1 << endl;
	}
	return 0;
}