#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define m 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
using namespace std;
int main()
{
	int t,count;
	scanf("%d",&t);
	count=1;
	while(t--)
	{
		printf("Case #%d: ",count);
		count++;
		priority_queue<pair<int,char> > pq;
		int n,i,x;
		char c;
		scanf("%d",&n);
		i=0;
		while(i<n)
		{
			scanf("%d",&x);
			c=(char)(i+'A');
			pq.push(make_pair(x,c));
			i++;
		}
		while(!pq.empty())
		{
			printf("%c",pq.top().second);
			if(pq.top().first>1)
				pq.push(make_pair(pq.top().first-1,pq.top().second));
			pq.pop();
			if(pq.size()==2 && pq.top().first==1)
			{
			}
			else
			{
				printf("%c",pq.top().second);
				if(pq.top().first>1)
					pq.push(make_pair(pq.top().first-1,pq.top().second));
				pq.pop();
			}
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}
