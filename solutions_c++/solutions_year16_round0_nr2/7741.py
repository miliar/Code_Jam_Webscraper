#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int main()
{
	int test,t;
	scanf("%d",&test);
	
	for(t=1;t<=test;t++)
	{
		char str[109];
		scanf("%s",str);
		int count=0,i,len=strlen(str);
		
		for(i=0;i<len-1;i++)
		{
			if(str[i]!=str[i+1])
				count++;
		}
		if(str[len-1]=='-')
			count++;
		printf("Case #%d: %d\n",t,count);
	}
	return 0;
}
