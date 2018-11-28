#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

int T;
int smax;
string s;

int main() {
	cin >> T;
	
	for (int lacase = 1; lacase <= T; lacase++) {
		cin >> smax;
		cin >> s;
		
		int curtot = 0;
		int res = 0;
		
		for (int i = 0; i <= smax; i++)
			if (s[i] != '0') {
				int more = max(0, i - curtot);
				res += more;
				curtot += more + (s[i] - '0');
			}
		
		cout << "Case #" << lacase << ": " << res << "\n";
	}
	
	return 0;
}
