#define _CRT_SECURE_NO_DEPRECATE

#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int count=0;
	int t,num;
	char str[105];
	int num_exe=0;

	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );

	scanf("%d", &t);
	for (num = 1; num <= t; num++) {
		scanf("%s", str);
		count = 0;
		num_exe = 0;

		while (1) {
			if (str[count] != '\0') {
				count++;
			}
			else break;
		}

		while (1) {
			if (count == 0) break;
			if (str[count-1] == '+') {
				count--;
				continue;
			}
			else if(str[count-1] == '-') {
				for (int x = (count-1); x >= 0; x--) { //swap
					if (str[x] == '+')
						str[x] = '-';
					else
						str[x] = '+';
				}
			count--;
			num_exe++;
			}
		}

		printf("Case #%d: %d\n", num, num_exe);
	}

	return 0;
}