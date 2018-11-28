#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
	int T, N, i, j, temp, rem, flg, num;
	
	cin >> T;
	for (i = 1; i <= T; i++) {
		
		int a[10] = {0};
		
		cin >> N;
		
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i);
		}
		
		else {
			temp = N;
			flg = 0;
			
			for (j = 2; ; j++) {
				
				num = temp;
				
				while (temp != 0) {
					rem = temp % 10;
					temp = temp / 10;
					
					a[rem] = 1;
				}
				
				if (a[0] == 1 && a[1] == 1 && a[2] == 1 && a[3] == 1 && a[4] == 1 && a[5] == 1 && a[6] == 1 && a[7] == 1 && a[8] == 1 && a[9] == 1) {
					flg = 1;
					break;
				}	
				else
					temp = N * j;
			}
			
			if (flg = 1)
				printf("Case #%d: %d\n", i, num);
			else if (flg = 0)
				printf("Case #%d: INSOMNIA\n");
				
		}
	}
}
