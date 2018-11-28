#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <stack>
#include <cmath>
#include <bitset>
#include <queue>
#include <map>
#include <set>

using namespace std;

int T, maxS;
int ans;
char num_list;

int main()
{
	//freopen("A-large.in", "r", stdin);
	scanf("%d", &T);
	
	for(int i=0; i<T; i++)
	{
		ans = 0;
		scanf("%d", &maxS);
		int sum = 0;
		scanf(" %c", &num_list);
		sum += (num_list-'0');
		for(int j=1; j<maxS+1; j++)
		{
			scanf("%c", &num_list);
			
			if(sum < j)
			{
				ans += j - sum;
				sum += j - sum;
			}
			sum += (num_list-'0');
		}
		
		printf("Case #%d: %d\n", i+1, ans);
	}
	
	return 0;
}
