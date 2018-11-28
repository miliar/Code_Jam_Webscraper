#include <stdio.h>
#include <map>
using namespace std;

const int N = 4;
int s1[N][N];

map<int, int> vis;

int main () {

	int t, r1, r2;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++ ){
		
		scanf("%d", &r1);
		for (int j = 0; j < N; j++)
			for (int k = 0; k < N; k++)
				scanf("%d", &s1[j][k]);
		for (int j = 0; j < N; j++)
			vis[s1[r1 - 1][j]] = 1;
		scanf ("%d", &r2);
		for (int j = 0; j < N; j++)
			for (int k = 0; k < N; k++)
				scanf("%d", &s1[j][k]);
		int count = 0, ans;
		for (int j = 0; j < N; j++)
			if (vis[s1[r2 - 1][j]]) {

				count++;
				ans = s1[r2 - 1][j];
			}
		if (!count)
			printf("Case #%d: Volunteer cheated!\n", i);
		else if (count == 1)
			printf("Case #%d: %d\n", i, ans);
		else
			printf("Case #%d: Bad magician!\n", i);
		vis.clear();
	}
	return 0;
}
