#include <iostream>
#include <cstdio>
#include <time.h>
#include <stdlib.h>
using namespace std;

//char parsed[128];
string parsed;
char copyy[128];

// flip from 0 to limit
void flip (int limit) {
	for (int i = 0; i < limit; i++) {
		copyy[limit - 1 - i] = (parsed[i] == '+') ? '-' : '+';
	}
	
	for (int i = 0; i < limit; i++) {
		parsed[i] = copyy[i];
	}
}

int main () {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	srand(time(NULL));
	
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cin >> parsed;
		
		int result = 0;
		for (int d = (int) parsed.size() - 1; d >= 0; d--) {
			if (parsed[d] == '+') {
				continue;
			}
				
			if (parsed[d] == '-' && parsed[0] == '-') {
				flip(d+1);
				result++;
				continue;
			}
				
			if (parsed[d] == '-' && parsed[0] == '+') {
				for (int prefix = 0; prefix <= d; prefix++) {
					if (parsed[prefix] == '-') {
						flip(prefix);
						break;
					}
				}
				flip(d+1);
				result += 2;
			}
		}
		
		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}

