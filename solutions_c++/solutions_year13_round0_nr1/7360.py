#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

#define MAX 4

int main () {

	int cases = 1, i, j, add, res, tmp;
	int l[MAX], c[MAX], d[MAX], flag;
	char s;

	scanf("%d", &i);
	scanf("%c", &s);
	while (i--) {

		for (j = 0; j < MAX; j++)
			l[j] = c[j] = d[j] = 0;

		flag = 0;
		for (j = 0; j < MAX*MAX; j++) {
			scanf("%c", &s);
			if (s == '\n')
				scanf("%c", &s);
			if (s == 'X') add = 1;
			else if (s == 'O') add = -1;
			else if (s == 'T') add = 0;
			else {add = -50; flag = 1;}

			l[j/MAX] += add;
			c[j%MAX] += add;

			if (j == 0 || j == 5 || j == 10 || j == 15)
				d[0] += add;
			if (j == 3 || j == 6 || j == 9 || j == 12)
				d[1] += add;
		}
		scanf("%c", &s);

		res = 0;
		for (j = 0; j < MAX; j++) {
			if (abs(l[j]) == 3 || abs(l[j]) == 4)
				res = (l[j] > 0) ? 1 : -1;
			else if (abs(c[j]) == 3 || abs(c[j]) == 4)
				res = (c[j] > 0) ? 1 : -1;
		}

		if (abs(d[0]) == 3 || abs(d[0]) == 4)
			res = (d[0] > 0) ? 1 : -1;
		else if (abs(d[1]) == 3 || abs(d[1]) == 4)
			res = (d[1] > 0) ? 1 : -1;

		printf("Case #%d: ", cases++);
		if (res == 1) printf("X won\n");
		else if (res == -1) printf("O won\n");
		else {
			if (!flag) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}

	return 0;
}
