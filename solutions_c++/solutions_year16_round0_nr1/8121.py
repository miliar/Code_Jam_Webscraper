#define _CRT_SECURE_NO_DEPRECATE

#include<stdio.h>
#include<iostream>
#include <stdlib.h>
#include<string.h>

using namespace std;

int main()
{
	int count,t,num;
	int in=0,n=0,real_in=0;
	bool least[10];
	char leastt[1000005];
	int truth = 0;
	int mul = 2;

	freopen( "A-large.in", "r", stdin );
	freopen( "A-large1.txt", "w", stdout );

	scanf("%d", &t);
	for (num = 1; num <= t; num++) {
		scanf("%d", &in);
		real_in = in;
		for (int x = 0; x < 10; x++)
			least[x] = false;
		mul = 2;
		sprintf(leastt, "%d", in);

		if (in == 0) {
			printf("Case #%d: INSOMNIA\n", num);
			continue;
		}

		while (1) {
			int f = 0;
			while (1) {
				if (leastt[f] == '\0')	break;
				else {
					int cur_num = leastt[f] - '0';
					least[cur_num] = true;
				}
				f++;
			}

			truth = 1; // check
			for (int g = 0; g <= 9; g++){
				if (least[g] == false) truth = 0;
			}

			if (truth == 1) {
				printf("Case #%d: %d\n", num, in);
				break;
			}
			else {
				in = real_in * mul; mul++;
				sprintf(leastt, "%d", in);
			}
		}
	}

	return 0;
}