#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
using namespace std;

#define N 4

int Case;
int a[N][N], b[N][N];
int ra, rb;


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &Case);
	for (int tt = 1; tt <= Case; ++tt){
		scanf("%d", &ra);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				scanf("%d", &a[i][j]);
		scanf("%d", &rb);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				scanf("%d", &b[i][j]);
		ra--; rb--;
		int num = 0;
		int ans = -1;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				if (a[ra][i] == b[rb][j]) { num++; ans = a[ra][i]; }
		printf("Case #%d: ", tt);
		if (num == 0) printf("Volunteer cheated!\n");
		else if (num > 1) printf("Bad magician!\n");
		else printf("%d\n", ans);
		}
	return 0;
	}
