#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<limits.h>

int main()
{
    int k,r,t,p,cnt,c=0;
	freopen("c.in","r",stdin);
	freopen("cc.out","w",stdout);
	scanf("%d",&k);
	while(k--)
	{
		cnt=0;c++;
		scanf("%d%d",&r,&t);
		for(int i=1;;i+=2)
		{
			p=(r+i)*(r+i)-(r+i-1)*(r+i-1);
			if(p<=t)
			{
				cnt++;
				t-=p;
			}
			else 
			break;
			
		}
		printf("Case #%d: %d\n",c,cnt);
		
	}
}
