#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int hash[19];
int main()
{
	int t,test,in,i,j,num;
	scanf("%d",&test);
    for(t=1;t<=test;t++)
    {
    	scanf("%d",&in);
    	for(i=1;i<=16;i++)hash[i]=0;
    	for(i=1;i<=4;i++)
    	{
    		for(j=1;j<=4;j++)
    		{
    			scanf("%d",&num);
    			if(i==in)
    			hash[num]++;
    		}
    	}
    	scanf("%d",&in);
    	for(i=1;i<=4;i++)
    	{
    		for(j=1;j<=4;j++)
    		{
    			scanf("%d",&num);
    			if(i==in)
    			hash[num]++;
    		}
    	}
    	num=0;int ans;
    	for(i=1;i<=16;i++)
    	{
    		if(hash[i]==2)
    		{
    			num++;
    			ans=i;
    		}
    	}
    	printf("Case #%d: ",t);
    	if(num==0)
    	printf("Volunteer cheated!\n");
    	else if(num==1)
    	printf("%d\n",ans);
    	else
    	printf("Bad magician!\n");
    }
	return 0;
}
