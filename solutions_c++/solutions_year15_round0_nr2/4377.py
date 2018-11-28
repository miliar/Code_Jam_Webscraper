#include <cstdio>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

typedef pair<int,int> ii;
typedef pair<ii,int> iii;

int array[2000];

int main()
{
	int t;
	scanf("%d",&t);

	for(int casenum=1; casenum<=t; casenum++)
	{
		int n;
		scanf("%d",&n);

		int maxp = 0;

		for(int i=0; i<n; i++)
		{
			scanf("%d",array+i);
			maxp = max(maxp,array[i]);
			//printf("%d ",array[i]);
		}
		//puts("");

		priority_queue<iii,deque<iii>,greater<iii> > pq;
		for(int i=1; i<=maxp; i++)
			pq.push(iii(ii(0,0),i));
		int answer;

		while(pq.size())
		{
			iii temp = pq.top();
			pq.pop();

			int cost = temp.first.first;
			int pos = temp.first.second;
			int res = temp.second;

			//printf("%d %d %d\n",pos,res,cost);

			if(pos==n)
			{
				pq.push(iii(ii(cost+res,-1),0));
				continue;
			}
			if(pos==-1)
			{
				answer = cost;
				break;
			}

			pq.push(iii(ii(cost+(array[pos]-1)/res,pos+1),res));
		}

		printf("Case #%d: %d\n",casenum,answer);
	}

	return 0;
}