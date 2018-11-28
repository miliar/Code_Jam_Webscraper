//shashwat001

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

#define INF 2147483647
#define LINF 9223372036854775807
#define mp make_pair
#define pb push_back

typedef long long int lli;
typedef pair<int,int> pi;

int main ()
{
	int t,i,j,k,d[200],a;
	scanf("%d",&t);
	for (unsigned int T = 1; T <= t; T += 1)
	{
		fill(d,d+100,0);
		cin>>a;
		for(i = 0;i < 4;i++)
		{
			for(j = 0;j < 4;j++)
			{
				scanf("%d",&k);
				if(a == i+1)
				{
					d[k] += 1;
				}
			}
		}
		cin>>a;
		for(i = 0;i < 4;i++)
		{
			for(j = 0;j < 4;j++)
			{
				scanf("%d",&k);
				if(a == i+1)
				{
					d[k] += 1;
				}
			}
		}
		int cnt = 0;
		int idx;
		for(i = 1;i <= 16;i++)
		{
			if(d[i]==2)
			{
				cnt++;
				idx = i;
			}
		}
		printf("Case #%d: ",T);
		if(cnt==0)
		{
			printf("Volunteer cheated!\n");
		}
		else if(cnt==1)
		{
			printf("%d\n",idx);
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
