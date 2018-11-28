#include <stdio.h>
#include <string.h>

#define FOR(a, b) for(a=1;a<=b;a++)

char str[101][101];

int Moves()
{

	int i, j, m;

	i= j= m = 0;

	while (1) {

		/*if (str[0][i] == '\0') {
			
			if (str[1][j] != '\0')
				m += (strlen(str[1]) - j - 1);
			break;
		}
		else if (str[1][j] == '\0') {
			 
			if (str[0][i] != '\0')
				m += (strlen(str[0]) - i - 1);
			break;
		}*/

		if (str[0][i] == '\0' && str[1][j] == '\0')
			break;

		if (str[0][i] != str[1][j]) {

			while (str[0][i] == str[0][i - 1] && i > 0) {
				m++;
				i++;
			}

			while (str[1][j] == str[1][j - 1] && j > 0) {
				m++;
				j++;
			}
		}
		else {

			i++;
			j++;
		}


	}

	return m;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);

	freopen("A-small-attempt0.out", "w", stdout);

	int tc, i, j, k, n, m, l, x, flag;
	
	char comm[2][101];

	scanf("%d", &tc);

	FOR(i, tc) {

		scanf("%d", &n);

		scanf("%s", str[0]);

		l = strlen(str[0]);
		flag = x = 0;
		

		comm[0][x] = str[0][0];

		FOR(k, l) {

			if (comm[0][x] != str[0][k])
				comm[0][++x] = str[0][k];
		}

		scanf("%s", str[1]);

		l = strlen(str[1]);
		x = 0;

		comm[1][x] = str[1][0];

		FOR(k, l) {

			if (comm[1][x] != str[1][k])
				comm[1][++x] = str[1][k];
		}
		
		if (strcmp(comm[0], comm[1]) != 0)
			flag = 1;
		else {

			m = Moves();
		}


		if (flag == 1)
			printf("Case #%d: Fegla Won\n", i);
		else
			printf("Case #%d: %d\n", i, m);
	}


	return 0;
}