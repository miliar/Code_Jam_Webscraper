#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	
	int i,t,smax,k,sum,s,ans;
	char str[1003];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		sum=ans=0;
		scanf("%d",&smax);
		scanf("%s",&str);
		for(k=0;k<=smax;k++)
		{
			s=str[k]-'0';
			if(sum+ans<k)
			{
				ans+=(k-sum-ans);
			}
			sum+=s;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}