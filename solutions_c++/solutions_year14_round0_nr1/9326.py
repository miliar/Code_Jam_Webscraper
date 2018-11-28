#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define pb push_back
#define fs first
#define sc second
#define openfile {freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);}
#define debug 01

int main()
{
   if (debug) openfile;

	int te, ans, a[6][6];
	bool res[20];
	scanf("%d", &te);
	for (int t = 1; t <= te; t++)
	{
		scanf("%d", &ans);
		for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
		{
			scanf("%d", &a[i][j]);
			res[a[i][j]] = i == ans;
		}
		scanf("%d", &ans);
		int x = 0, y;
		for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
		{
			scanf("%d", &a[i][j]);
			if (!res[a[i][j]]) continue;
			res[a[i][j]] = i == ans;
			if (res[a[i][j]])
			{
				if (!x) y = a[i][j];
				x++;
			}
		}

		printf("Case #%d: ", t);
		if (!x) puts("Volunteer cheated!");
		else if (x > 1) puts("Bad magician!");
		else printf("%d\n", y);
	}

   return 0;
}
