#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <time.h>
#include <map>
using namespace std;
const int INF = 1e9;
const int N = 1001;

bool q[5][5][5];

int main()
{
	for (int j = 1; j <= 4; j++)
		for (int k = 1; k <= 4; k++)
			q[1][j][k] = true;



	q[2][1][1] = false;
	q[2][1][2] = true;
	q[2][1][3] = false;
	q[2][1][4] = true;
	q[2][2][1] = true;
	q[2][2][2] = true;
	q[2][2][3] = true;
	q[2][2][4] = true;
	q[2][3][1] = false;
	q[2][3][2] = true;
	q[2][3][3] = false;
	q[2][3][4] = true;
	q[2][4][1] = true;
	q[2][4][2] = true;
	q[2][4][3] = true;
	q[2][4][4] = true;


	q[3][3][2] = q[3][2][3] = true;
	q[3][3][3] = true;
	q[3][4][3] = q[3][3][4] = true;
	
	q[4][4][4] = true;
	q[4][4][3] = q[4][3][4] = true;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		
		printf("Case #%d: ", i);
		if (q[x][r][c])
			puts("GABRIEL");
		else
			puts("RICHARD");
	}
	return 0;
}
