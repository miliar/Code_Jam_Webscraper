#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	int t, n;
	string s;
	cin >> t;
	for(int cas = 0; cas<t; cas++) {
		cin >> s;
		int flips = 0;
		if (s[0] == '-') {
			flips = -1;
		}
		n = s.length();
		for (int i=0; i<n; ++i) {
			if (s[i] == '+') {
				continue;
			} else if (s[i] == '-'){
				while ((i+1 < n) && (s[i+1] == '-')) {
					++i;
				}
				flips += 2;
			}
		}
		cout << "Case #"<< (cas+1) <<": " << flips << endl;
	}
	return 0;
}