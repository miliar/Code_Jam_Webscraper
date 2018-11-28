#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
using namespace std;

bool isvowel(char s)
{
	if (s == 'a' || s == 'e' || s == 'i' || s == 'o' || s == 'u') {
		return true;
	}
	return false;
}


int main()
{
	int n, i, j, k, t, u = 1;
	cin >> t;
	string s;
	while (t--) {
		cin >> s >> n;
		int sm = 0;
		int c = 0;
		int l = s.size();
		//cout << s << "  " << n << endl;
		for (i = 0; i < l; i++) {
			for (j = i + n; j <= l; j++) {
				c = 0;
				for (k = i; k < j; k++) {
					//cout << s[k] << endl;
					if (isvowel(s[k])) {
						c = 0;
					} else {
						c++;
					}
					if (c >= n) {
						sm++;
						break;
					}
				}
			}
		}
		cout << "Case #" << u++ << ": " << sm << endl;

	}
	return 0;
}
