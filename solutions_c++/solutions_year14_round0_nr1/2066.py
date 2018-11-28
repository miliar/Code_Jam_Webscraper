#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-x))

int n = 4;
int r1, r2;
int a1[10][10], a2[10][10];


int main() 
{
	int T, cases = 0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &r1);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				scanf("%d", &a1[i][j]);
		scanf("%d", &r2);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				scanf("%d", &a2[i][j]);
		int sum = 0;
		int answer;
		for (int j1 = 1; j1 <= n; ++j1)
			for (int j2 = 1; j2 <= n; ++j2)
				if (a1[r1][j1] == a2[r2][j2]) 
				{
					++sum;
					answer = a1[r1][j1];
				}
		printf("Case #%d: ", ++cases);
		if (sum == 1) printf("%d\n", answer);
		else if (sum > 1) printf("Bad magician!\n");
		else if (sum == 0) printf("Volunteer cheated!\n");
	}
	return 0;
}

