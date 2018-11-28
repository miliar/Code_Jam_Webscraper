#include<iostream>
#include<stdio.h>
#include<cmath>
#include<vector>
using namespace std;
int main()
{
	int t,smax,sum,count,i,round;
	scanf("%d",&t);
	round=0;
    while(t--)
    {
    	round++;
    	scanf("%d",&smax);
    	char str[smax+5];
    	scanf("%s",str);
    	sum=0;count=0;
    	for(i=0;i<smax+1;i++)
    	{
    		if(str[i]=='0')
    			continue;
    		if(sum>=i)
    			sum+=str[i]-'0';
    		else
				{
					count+=(i-sum);
					sum=i+str[i]-'0';
				}	
    	}
    	printf("Case #%d: %d\n",round,count);	
    }
    return 0;
}
