#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
const int N = 10+10;
int a[N];
int b[N];
int main()
{
	int T;
	int x,y;
	scanf("%d",&T);
	int p = 1;
	while(T --)
	{
		map<int,int>mp;
		mp.clear();
		scanf("%d", &x);
		for(int i = 0; i < 16; i++)
		{
			scanf("%d", &a[i]);
		}
		for(int j = 4*(x-1); j < 4*(x-1)+4; j++)
			mp[a[j]] = 1;
		scanf("%d", &y);
		for(int i = 0; i < 16; i++)
			scanf("%d", &b[i]);
		int uniqCnt = 0;
		int uniqVal;
		for(int j = 4*(y-1); j < 4*(y-1)+4; j++)
		{
			// printf("b: %d\t", b[j]);
			if(mp[b[j]]==1)
			{
				uniqCnt++;
				uniqVal = b[j];
			}
		}
	
		if(uniqCnt == 1)
		{
			printf("Case #%d: %d\n",p++,uniqVal);
		}
		else if(uniqCnt>1)
		{
			printf("Case #%d: Bad magician!\n",p++);
		}
		else if(uniqCnt==0)
		{
			printf("Case #%d: Volunteer cheated!\n",p++);
		}

	}
	return 0;
}