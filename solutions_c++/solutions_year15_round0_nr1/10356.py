#include <bits/stdc++.h>
using namespace std;
int main()
{
	int test,i,num,temp,sum,ans,count,j;
	char str[10000];
	scanf("%d",&test);
	for(j=1;j<=test;j++)
	{
		scanf("%d",&num);
		scanf("%s",&str);
		count=sum=temp=ans=0;
		for(i=0;i<=num;i++)
		{
			temp=str[i]-'0';
			//cout<<temp<<endl;	
			if(temp==0);
			else
			{
				
				 
				 
				 sum=count-i;
				 if(sum>=0);
				 	
				 else
					{
						ans+=i-count;
						
						count+=(i-count);
					}	
					count+=temp;
					//cout<<count<<" "<<i<<endl;			 
			}
			
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}
