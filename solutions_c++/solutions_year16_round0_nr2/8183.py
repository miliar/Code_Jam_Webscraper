#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
	int T, i, j, l, count;
	
	cin >> T;
	
	for (i = 1; i <= T; i++) {
		
		char c[110];
		
		cin >> c;
		l = strlen(c);
		
		count = 0;

		for (j = l - 1; ; j--) {
			if (c[j] == '-') {
				for (int k = 0; k <= j; k++) {
					if (c[k] == '+')
						c[k] = '-';
					else if (c[k] == '-')
						c[k] = '+';
				}
				
				count++;
			}
			
			if (j == 0)
				break;
		}
		
		printf("Case #%d: %d\n", i, count);
		
	}
	
	return 0;
}
