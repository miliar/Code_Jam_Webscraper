#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <time.h>

#define SQR(_x) ((_x)*(_x))
#define NL printf("\n")
#define LL long long
#define DB double
#define PB push_back
#define INF 1<<30
#define LB lower_bound
#define UB upper_bound
#define F front
#define PQ priority_queue

using namespace std;

int main()
{
	int n,x;
	int c,temp,div,l,ans;
	int count,sth;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		int check[11]={0};
		count=0;
		scanf("%d",&x);
		if(x<10)
		{
			check[x]++;
			count++;
		}
		if(x==0) printf("Case #%d: INSOMNIA\n",i);
		else
		{
			c=1;
			
			while(1)
			{

				temp=x*c;
				div=1;
				while(temp/div>0)
				{
					sth=(temp%(div*10))/div;
					if(check[sth]==0)
					{
						check[sth]++;
						count++;
					}
					div*=10;

				}
				sth=temp/(div/10);
				if(check[sth]==0)
					{
						check[sth]++;
						count++;
					}
				if(count==10)
				{
					ans=temp;
					break;
				}
				c++;

			}
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}