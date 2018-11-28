#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define pi acos(-1.0)

int a[4][4];
int cnt[20];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		memset(cnt, 0, sizeof(cnt)); 
		for(int k = 0; k < 2; k++)
		{
			int row;
			scanf("%d", &row);
			row--;
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					scanf("%d", &a[i][j]);
			for(int i = 0; i < 4; i++)
				cnt[a[row][i]]++;
		}
		int res = 0, card = 0;
		for(int i = 1; i <= 16; i++)
			if(cnt[i] == 2)
				res++, card = i;

		if(res == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else
			if(res == 1)
				printf("Case #%d: %d\n", t, card);
			else
				printf("Case #%d: Bad magician!\n", t);
	}
	return 0;
}