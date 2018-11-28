#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

using namespace std;

int main(int argc, const char * argv[]) {
	int t_c = 0;
	cin >> t_c;
	for (int z = 1; z <= t_c; z++) {
		int k, count = 0, flag = 0;
		string s;
		cin >> s >> k;
		for (int i = 0; i < s.size() - k + 1; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				count++;
			}
		}
		for (int i = s.size() - k + 1; i < s.size(); i++) if (s[i] == '-') flag = 1;
		
		cout << "Case #" << z << ": ";
		if (flag == 1) cout << "IMPOSSIBLE" << endl;
		else cout << count << endl;
	}
	return 0;
}