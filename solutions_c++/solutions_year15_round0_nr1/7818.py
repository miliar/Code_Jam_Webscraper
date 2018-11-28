#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,d;
	d=1;
	scanf("%lld",&t);
	while(d<=t)
	{
		long long int n;
		scanf("%lld",&n);
		char str[n+1];
		scanf("%s",str);
		long long int sum,count=0,i,j,k,min,max;
		i=1;
		sum=str[0]-'0';
		while(str[i]!='\0')
		{
			
		     if(str[i]!='0')
		     {
		        if(sum<i)
				{
					count=count+(i-sum);
					sum=sum+i-sum;
				} 	
		     }
		     sum=sum+(str[i]-'0');
		     i++;
			  
		}
		printf("Case #%lld: %lld\n",d,count);
		d++;
	}
	return 0;
}
