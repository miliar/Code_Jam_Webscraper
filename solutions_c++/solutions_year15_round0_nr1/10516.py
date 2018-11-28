//PROBLEM A
#include<cstdio>
using namespace std;
int main ()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		int n,total,c=0;
		scanf("%d",&n);
		char x[n+5];
		scanf("%s",x);
		total = ((int)x[0]-48);
		for(int j=1;j<=n;j++)
		{
			if (total>=j) total+=((int)x[j]-48);
			else if (total<j&&(int)x[j]==48);
			else
			{
				while(total<j)
				{
					c++;
					total++;
				}
				total+=((int)x[j]-48);
			}
		}
		printf("Case #%d: %d\n",i,c);
	}
	return 0;
}
