/* Infinite House Of Pancakes
 * CodeJam 2015
 * Google
 * Date : 11/04/2015
 */
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;
typedef long long ll;

const ll MAX = 1002;
ll pp[MAX][MAX];

//preprocessing 
void preprocess()
{
	ll i = 1;
	for (ll i = 1; i < MAX; i++)
	{	
		for (ll j = 0; j < MAX && j < i; j++)
		{	
			if (j == 0) pp[i][j] = i;
			else
			{
				ll div = i / (j+1);
				ll rem = i % (j+1);
				if (rem == 0)
					pp[i][j] = div;
				else
					pp[i][j] = pp[rem][rem - 1] + div;
			}
		}
	}
}

struct NodeC
{
	ll spMin,count,value;
	NodeC() { spMin = 0;count = 0;value = 0;}
	bool operator > (const NodeC& r) const { return value < r.value;}	
};

ll findMinimumTime(priority_queue<NodeC, vector<NodeC>, greater<NodeC> >& pq)
{
	ll numberOfTimes = 0;	
	NodeC top = pq.top();
	ll minTime = top.value;
	while (numberOfTimes < minTime)
	{
		top = pq.top();
		pq.pop();
		top.spMin++;
		top.value = pp[top.count][top.spMin];
		if (top.count - 1 < top.spMin) break;
		pq.push(top);
		numberOfTimes++;
		if (numberOfTimes + pq.top().value < minTime)
			minTime = numberOfTimes + pq.top().value;
	}
	return minTime;
}

int main()
{
	ll t,d,p;
	scanf("%lld",&t);
	preprocess();
	for (ll j = 1; j <= t; j++)
	{	//priority queue of NodeC
		priority_queue < NodeC, vector<NodeC>, greater<NodeC>  > pq;
		scanf("%lld", &d);
		for (ll i = 0; i < d; i++)
		{
			scanf("%lld", &p);
			NodeC node;
			node.count = p; node.spMin = 0; node.value = pp[p][0];
			pq.push(node);
		}
		ll minTime = findMinimumTime(pq);
		printf("Case #%lld: %lld\n",j, minTime);
	}
	return 0;
}
