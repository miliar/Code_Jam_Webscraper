#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int tt;
char s[107];

int main() {
	ios_base::sync_with_stdio(0);
	cin >> tt;
	int nrr = 1;
	while(tt--) {
		cin >> s;
		int n = 0;
		while(s[n]) n++;
		s[n] = '+';
		n++;
		int w = 0;
		char zn;
		for(int i = 0; i < n; ++i) {
			if(i > 0 && s[i] != zn) w++;
			zn = s[i];
		}
		cout << "Case #" << nrr << ": " << w << '\n';
		nrr++;
	}
	//system("pause");
	return 0;
}