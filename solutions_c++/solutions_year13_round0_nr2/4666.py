#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAX 110 

int n, m;
int a[MAX][MAX], c[MAX][MAX];

int main () {
	int teste;
	scanf ("%d", &teste);
	for (int t = 0; t < teste; t++) {
		scanf ("%d %d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				scanf ("%d", &a[i][j]);
				c[i][j] = 100;
			}
		for (int i = 0; i < n; i++) {
			int maxi = 0;
			for (int j = 0; j < m; j++)
				maxi = max (maxi, a[i][j]);
			for (int j = 0; j < m; j++)
				c[i][j] = min (c[i][j], maxi);
		}
		for (int j = 0; j < m; j++) {
			int maxi = 0;
			for (int i = 0; i < n; i++)
				maxi = max (maxi, a[i][j]);
			for (int i = 0; i < n; i++)
				c[i][j] = min (c[i][j], maxi);
		}
		int flag = 1;
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < m; j++) 
				if (c[i][j] != a[i][j])
					flag = 0;

		printf ("Case #%d: ", t + 1);
		if (flag == 0)
			printf ("NO\n");
		else
			printf ("YES\n");

	}
	return 0;
}
