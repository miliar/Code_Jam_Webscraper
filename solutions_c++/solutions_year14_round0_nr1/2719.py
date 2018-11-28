#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int t;
	freopen("C:\\Users\\Prathma\\Downloads\\A-small-attempt1.in", "r", stdin);
	freopen("C:\\Users\\Prathma\\Desktop\\outputstr.txt", "w", stdout);
	
		scanf("%d", &t);
		int k = 1;
		while (t--) {
			int a[4][4], b[4][4], r1, r2, c = 0;
			scanf("%d", &r1);
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					scanf("%d", &a[i][j]);
				}
			}

			scanf("%d", &r2);
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					scanf("%d", &b[i][j]);
				}
			}
			int p;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (a[r1 - 1][i] == b[r2 - 1][j]) {
						c++;
						p = a[r1-1][i];
					}
				}
			}

			if (c == 0) {
				printf("Case #%d: Volunteer cheated!\n", k);
			}
			else if (c == 1) {
				printf("Case #%d: %d\n", k, p);
			}
			else if (c > 1) {
				printf("Case #%d: Bad magician!\n", k);
			}
			k++;

		}
		fclose(stdin);
		fclose(stdout);
	
	return 0;
}