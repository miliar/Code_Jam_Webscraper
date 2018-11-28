#include <bits/stdc++.h>		//ry

using namespace std;

int main()
{
	int test; 
	cin>>test;
	
	int Smax,garb;
	int cnt=0;
	
	for(int i=1;i<=test;i++)
	{
		cin>>Smax;
		
		if(Smax==0)
			{
				printf("Case #%d: 0\n",i);
				cin>>garb;
				continue;
			}
			
		int arr[7], num;
		
		cin>>num;
		
		for(int j=Smax;j>=0;j--)
		{
			arr[j]=(num%10);
			num=num/10;
			
		}

		cnt=arr[0];
		
		int req,res=0;
		
		for(int j=1;j<=Smax;j++)
		{
			req=0;
			if(j>cnt)
			{
				req=(j-cnt);
				res+=req;
			}
			
			cnt+=arr[j]+req;
		}
		
		printf("Case #%d: %d\n",i,res);
	}
	
return 0;
}