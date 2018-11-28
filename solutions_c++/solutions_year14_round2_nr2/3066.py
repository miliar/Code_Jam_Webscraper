#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
int main()
{
	
	int tt,n;
	//vector<string> d;
	scanf("%d",&tt);
	long int a,b,k,i,j,ans;long long int count=0;
	for(int qq=1;qq<=tt;qq++)
	{
		printf("Case #%d: ",qq);count=0;
		scanf("%ld%ld%ld",&a,&b,&k);
	//	if(k>=a)
	//	count=a*b;
//		else 
//		{
		//	count=(k*b)+((a-k)*k);
			//for(int i=k;i<a;i++)
			for(int i=0;i<a;i++)
			{
				//for(int j=k;j<b;j++)
				for(int j=0;j<b;j++)
				{
					if((i&j)<k)
					count++;
				}
	//		}
		}
		
		
		printf("%lld\n",count);
		}
		
		return 0;
	}	
