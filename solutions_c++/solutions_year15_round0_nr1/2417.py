#include<bits/stdc++.h>
using namespace std;
#define l int
 
l cas;
char st[1003];
l ran[1003];
int main()
{   freopen("inpu.txt","r",stdin);
	freopen("o.txt","w",stdout);
	l k,tc,i,val=0,man=0;
	
	scanf("%d",&tc);
	for(k=1;k<=tc;k++)
	{
		scanf("%d",&cas);
		scanf("%s",st);
		for(i=0;i<=cas;i++)
		{
			ran[i]=st[i]-'0';
		}
		val=ran[0];
		man=0;
		for(i=1;i<=cas;i++)
		{
			if(val<i)
			{
				man++;
				val++;
			}
			val+=ran[i];
		}
		printf("Case #%d: %d\n",k,man);
	}
	fclose(stdout);
	return 0;
}
