#include<stdio.h>
using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int smax,cur,persons=0,req=0;
		char s[1001];
		scanf("%d",&smax);
		scanf("%s",s);
		for(int i=0;i<smax+1;i++)
		{
			cur = s[i]-48;
			if(persons<i)
				{
				req+= i-persons;
				persons+=i-persons;
			}
			persons+=cur;
		}
		printf("Case #%d: %d\n",j,req);
	}
	return 0;
}
