#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define inf 0x3f3f3f3f
#define eps 1e-9
using namespace std;

int A[5][5], B[5][5];

int main()
{
	freopen("i.in", "rt", stdin);
	freopen("o.out", "wt", stdout);
	int t, xa, xb, i, j, test = 0;
	cin >> t;
	while(t--)
	{
		test++;
		scanf("%d", &xa);
		xa--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				scanf("%d", &A[i][j]);
		scanf("%d", &xb);
		xb--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				scanf("%d", &B[i][j]);
		int cnt = 0;
		int ans = 0;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				if(A[xa][i] == B[xb][j])
				{
					cnt++;
					ans = A[xa][i];
				}
		printf("Case #%d: ", test);
		if(cnt > 1)
			puts("Bad magician!");
		else
			if(cnt == 0)
				puts("Volunteer cheated!");
			else
				printf("%d\n", ans);
	}
}

