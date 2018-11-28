#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	freopen("B-large.in","r", stdin);
	freopen("b.out","w", stdout);
	int test,t;
	cin >> t;
	for (test = 1; test <= t; test++) {
		int ans = 0;
		string s;
		cin >> s;
		int n = s.size();
		for (int i = 0; i < n; i++) {
			while (s[i] == s[i+1]) {
				i++;
			}
			ans++;
		}
		if (s[s.size()-1] == '+'){
			cout << "Case #" << test << ": " << ans - 1  << endl;
		}
		else 
			cout << "Case #" << test << ": " << ans << endl;
	}


	return 0;
}