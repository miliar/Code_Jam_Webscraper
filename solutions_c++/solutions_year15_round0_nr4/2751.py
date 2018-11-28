#include <stdio.h>

int main()
{
	freopen("D-small-attempt4.in", "r", stdin);
	freopen("D-small-attempt4.out", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int T = 1; T <= t; T++){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);

		int a = r * c;
		printf("Case #%d: ", T);
		if (a%x)printf("RICHARD");
		else{
			if (x == 1)printf("GABRIEL");
			else if (x == 2){
				printf("GABRIEL");
			}
			else if (x == 3){
				if (!(c % 2) || !(r % 2))printf("GABRIEL");
				else if (c == 3 && r == 3)printf("GABRIEL");
				else // 1 * 3
					printf("RICHARD");
			}
			else if (x == 4){
				if (r == 4 && c >= 3 || r >= 3 && c == 4)printf("GABRIEL");
				else
					printf("RICHARD");
			}
		}
		printf("\n");
	}
	// ¹«Á¶°Ç x >= 7 richard win
}