#include <stdio.h>
#include <stdlib.h>
#include <set>

using namespace std;

int main()
{
	int T,c = 1;
	scanf("%d",&T);

	while(T--)
	{
		int A,B,K,count=0;

		set<pair<int,int> > myset;

		scanf("%d%d%d",&A,&B,&K);

		for(int i=0;i<K;i++)
		{
			for(int j=0;j<A;j++)
			{
				for(int p=0;p<B;p++)
				{
					if(i==(j&p))
					{
						count++;
					}
				}
			}
		}
		printf("Case #%d: %d\n",c++,count);
	}
	return 0;
}