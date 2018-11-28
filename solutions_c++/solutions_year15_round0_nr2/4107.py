#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <cstring>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
int d;
int p[1003];
int main()
{
	int t,ans,fix,temp,temp1,temp2,s;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&d);
		priority_queue<int> pq;
		for(int j=0;j<d;j++)
		{
			scanf("%d",&p[j]);
			pq.push(p[j]);
		}
		ans = pq.top();
		fix=0;
		while(pq.top()>3)
		{
			temp = pq.top();
			pq.pop();
			if(temp==9)
				temp1 = 6;
			else
				temp1 = temp/2;
			temp2 = temp - temp1;
			pq.push(temp1);
			pq.push(temp2);
			fix++;
			ans = min(ans,pq.top()+fix);
		}
		priority_queue<int> pq2;
		for(int j=0;j<d;j++)
		{
			pq2.push(p[j]);
		}
		fix=0;
		while(pq2.top()>3)
		{
			temp = pq2.top();
			pq2.pop();
			temp1 = temp/2;
			temp2 = temp - temp1;
			pq2.push(temp1);
			pq2.push(temp2);
			fix++;
			ans = min(ans,pq2.top()+fix);
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}