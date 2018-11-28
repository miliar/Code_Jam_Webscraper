#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>

#include <Windows.h>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int TC = 0;
	inf >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int l;
		string s;
		inf >> l >> s; 

		int num = s[0] - '0';
		int ans = 0; 
		for (int i = 1; i < s.size(); i++) {
			int n = s[i] - '0'; 
			if (n > 0) {
				if (i > num) {
					ans += (i - num);
					num += (i - num);
				}
				num += n;
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}

	return 0;
}