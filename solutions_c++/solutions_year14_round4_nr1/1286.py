#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
int T,n,k;
int size[10005];
int tmp[10005];
bool solve(int mid)
{
	int j = n-1;
	for (int i=0;i<mid;i++)
	{
		tmp[i] = k - size[j];
		j--;
	}
	int cur = 0;
	int res = 0;
	while(res <= j)
	{
		while(cur < mid && tmp[cur] < size[res])
		{
			cur ++;
		}
		if (cur >=mid)
			break;
		res ++;
		cur ++;
	}
	return res > j;
}
int main()
{
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		for (int j=0;j<n;j++)
		{
			scanf("%d", &size[j]);
		}
		sort(size, size+n);
		int left = 1;
		int right = n;
		while(left<right)
		{
			int mid = (left+right)/2;
			if (solve(mid))
				right = mid;
			else
				left = mid + 1;
		}
		printf("%d\n",left);
	}
	return 0;
}