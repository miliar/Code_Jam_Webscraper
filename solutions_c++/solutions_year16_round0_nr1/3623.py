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
        long long n_orig, n;
		cin >> n_orig;
		long long res = -1;

		if (n_orig > 0) {
			n = 0;
			map<char, char> digit;
			
			for (int i = 0; i < 100; i++) {
				n += n_orig;
				
				if (done(n, digit)) {
					break;
				}
			}
			
			res = n;
		}
		
		cout << "Case #" << (tc_i + 1) << ": ";
		
		if (res > -1) {
			cout << res;
		}
		else {
			cout << "INSOMNIA";
		}

		cout << endl;
    }

    return 0;
}