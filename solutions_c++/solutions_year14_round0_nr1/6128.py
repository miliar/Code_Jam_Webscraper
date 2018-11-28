// MagicTrick.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int t;
	scanf("%d", &t);
	while (t--) {
		static int id = 0;
		int n; 
		scanf("%d", &n);
		int temp;
		int b1[4];
		int b2[4];
		for (int r=1; r<5; r++) {
			for (int c=0; c<4; c++) {
				if (r==n) {
					scanf("%d", &b1[c]);
				} else {
					scanf("%d", &temp);
				}
			}
		}
		scanf("%d", &n);
		for (int r=1; r<5; r++) {
			for (int c=0; c<4; c++) {
				if (r==n) {
					scanf("%d", &b2[c]);
				} else {
					scanf("%d", &temp);
				}
			}
		}
		bool match = false;
		bool flag = false;
		int solution;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (b1[i] == b2[j]) {
					if (match) {
							printf("Case #%d: Bad magician!\n", ++id);
							flag = true;
							break;
					} else {
						solution = b1[i];
						match = true;
					}
				}
				if (flag) {break;}
			}
			if (flag) {break;}
		}
		if (match && !flag) {
			printf("Case #%d: %d\n", ++id, solution);
		} else if (!flag) {
			printf("Case #%d: Volunteer cheated!\n", ++id);
		}
	}

	
	return 0;
}

