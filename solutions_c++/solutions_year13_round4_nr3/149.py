
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>


using namespace std;
int n;
		int a [10000];
		int b [10000];
int used[300];
int anw[300];
int dp[300];
int dpx[300];
bool found;
void go (int from)
{
	if (found )
		return;
	if ( from == n+1)
	{
		
		for (int i = n; i >= 1; i--)
		{
			int bst = 1;
			for (int j = i+1; j <= n; j++)
				if( anw[j] < anw[i])
					bst = max(bst,dp[j] + 1);
			if (b[i] != bst)
				return;
			dp[i] = bst;

		}
		found = 1;
		return;
	}
	for (int i = 1; i <= n; i++)
		if (! used[i])
		{
		
			if (found)
				return;
			int bst = 1;
			for (int j = 1; j < from; j++)
			{
				if (anw[j] < i)
					bst = max(bst, dp[j] + 1);
			}
			if (bst == a[from])
			{
				used[i] = 1;
				dp[from] = bst;
				anw[from] = i;
				go (from + 1);
			}
			used[i] = 0;
		}
}
int main()
{
	freopen("input.txt","rt", stdin);
	freopen("output.txt","wt", stdout);			
	int tests;
	scanf("%d\n", &tests);	
	long long pp = 1000002013;
	int o, e, p;
	//for (int i = 0; i < 3000; i++)
	for (int test = 1; test <= tests; test++)
	{

		scanf("%d ", &n, &p);		

		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]);
		}
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &b[i]);
		}
		memset(used, 0, sizeof(used));
		found = 0;
		go (1);
		

		printf("Case #%d: ",test);		
		for (int i = 1; i <= n; i++)
			printf("%d ", anw[i]);
		printf("\n");

	}
		
	return 0;			
}     
