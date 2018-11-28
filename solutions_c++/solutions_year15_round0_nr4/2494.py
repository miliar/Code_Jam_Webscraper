#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ("D-small-attempt2.in","r",stdin);
	freopen ("myfile.txt","w",stdout);
	int T;
	cin >> T;
	int x = 1;
	while (x <= T) {
		int a, b, c;
		cin >> a >> b >> c;
		if ( (b * c)  % a != 0 || (a > b && a > c) || a >= 7) {
			printf("Case #%d: RICHARD\n", x);
			x++;
			continue;
		}
		if (a == 1 || a == 2) {
			printf("Case #%d: GABRIEL\n", x);
			x++;
			continue;
		}
		if (a == 3) {
			if (b != 1 && c != 1) {
				printf("Case #%d: GABRIEL\n", x);
				x++;
				continue;	
			}
			else {
				printf("Case #%d: RICHARD\n", x);
				x++;
				continue;	
			}
		}
		else {
			if (b <= 2 || c <= 2) {
			printf("Case #%d: RICHARD\n", x);
			x++;
			continue;
			}
		}
		// a == 4
		
		
		
		
		
		
		printf("Case #%d: GABRIEL\n", x);
		x++;
	}
}
