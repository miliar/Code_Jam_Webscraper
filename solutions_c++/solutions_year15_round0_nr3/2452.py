#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;

int L, X;
char SO[10010];
char S[10010];
char M[10010][10010];

#define I 2
#define J 3
#define K 4

const int T[5][5] = {
	{0, 0,  0,  0,  0},
	{0, 1,  I,  J,  K},
	{0, I, -1,  K, -J},
	{0, J, -K, -1,  I},
	{0, K,  J, -I, -1}
};

int mult(int a, int b)
{
	if (a > 0 && b > 0)
		return T[a][b];
	if (a > 0 && b < 0)
		return -T[a][-b];
	if (a < 0 && b > 0)
		return -T[-a][b];
	return T[-a][-b];
}

bool solve()
{
	for (int i = 1; i < L-1; i++) {
		for (int j = i+1; j < L; j++) {
			if (M[0][i-1] == I &&
				M[i][j-1] == J &&
				M[j][L-1] == K)
				return true;
//			printf("(%d %d / %d %d / %d %d)\n", 0, i-1, i, j-1, j, L-1);
		}
	}
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &L, &X);
		scanf("%s", SO);
		for (int i = 0; i < X; i++)
			strcpy(S+i*L, SO);
		L *= X;

		for (int i = 0; i < L; i++) {
			M[i][i] = S[i]-'g';
			for (int j = i+1; j < L; j++) {
				M[i][j] = mult(M[i][j-1], S[j]-'g');
			}
		}
/*
		for (int i = 0; i < L; i++) {
			for (int j = i; j < L; j++)
				printf("%d ", M[i][j]);
			printf("\n");
		}
		*/

		printf("Case #%d: %s\n", t, solve() ? "YES" : "NO");
	}
	return 0;
}
