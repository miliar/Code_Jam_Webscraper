#include <iostream>
#include <stdio.h>
using namespace std;

#define MAXN 100

int RowMax [MAXN];
int ColMax [MAXN];
int Lawn [MAXN][MAXN];

int main () {
	int T, N, M;
	
	scanf ("%d", &T);
	
	for (int tc = 1; tc <= T; tc++) {
		scanf ("%d %d", &N, &M);
		
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				scanf ("%d", &Lawn [i][j]);
				
		for (int i = 0; i < N; i++) {
			RowMax [i] = Lawn [i][0];
			for (int j = 1; j < M; j++) 
				RowMax [i] = max (RowMax [i], Lawn [i][j]);
		}
		
		for (int j = 0; j < M; j++) {
			ColMax [j] = Lawn [0][j];
			for (int i = 1; i < N; i++) 
				ColMax [j] = max (ColMax [j], Lawn [i][j]);
		}
		
		bool possible = true;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (Lawn [i][j] < RowMax [i] && Lawn [i][j] < ColMax [j])
					possible = false;
			}
		}
		
		if (possible)
			printf ("Case #%d: YES\n", tc);
		else
			printf ("Case #%d: NO\n", tc);
	}
	
	return 0;
}
