#include <cstdio>
using namespace std;

int main()
{
	const int m = 4;
	int a[m * m];
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < m * m; j++) {
			a[j] = 0;
		}
		for (int l = 0; l < 2; l++) {
			int row;
			scanf("%i", &row);
			--row;
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < m; k++) {
					int x;
					scanf("%i", &x);
					if (j == row) a[x -1]++;
				}
			}
		}
		int cnt = 0;
		int pos = -1;
		for (int j = 0; j < m * m; j++) {
			if (a[j] == 2) {
				cnt++;
				pos = j;
			}
		}
		printf("Case #%i: ", i +1);
		if (cnt == 1)
			printf("%i", pos +1);
		else if (cnt == 0)
			printf("Volunteer cheated!");
		else
			printf("Bad magician!");
		printf("\n");
	}
	return 0;
}

