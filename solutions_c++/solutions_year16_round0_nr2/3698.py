#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007
#define MAXN 100001

#define PRIME 1000008259

using namespace std;

bool done (int n, map<char, char> &digit) {
	while (n) {
		int dig = n % 10;
		
		if (!digit[dig]) {
			digit[dig] = true;
			digit['x']++;
		}
		
		n /= 10;
	}
	
	return digit['x'] == 10;
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
	
    int tc;
	cin >> tc;
	
    for (int tc_i = 0; tc_i < tc; tc_i++) {
		string s;
		cin >> s;
		
		char last = s[0];
		s += 'x';
		int cnt = 0;
		int res;
		
		for (int i = 1; i < s.size(); i++) {
			if (s[i] != last) {
				cnt++;
				last = s[i];
			}
		}
		
		if (s[0] == '+') {
			if (cnt % 2 == 0) {
				res = cnt;
			}
			else {
				res = cnt - 1;
			}
		}
		else {
			cnt--;
			res = 1;
			
			if (cnt % 2 == 0) {
				res += cnt;
			}
			else {
				res += cnt - 1;
			}			
		}
		
		cout << "Case #" << (tc_i + 1) << ": ";
		cout << res;
		cout << endl;
    }

    return 0;
}