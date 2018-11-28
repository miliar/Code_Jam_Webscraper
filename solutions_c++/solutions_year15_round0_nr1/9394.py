#include <iostream>
#include<stdio.h>
using namespace std;
 
int main()
{
	int t,k=1;
	scanf("%d",&t);
	k=1;
	while(t--)
	{
		int a[10000],i,j,s,count=0,min=0;
		char str[10000];
		scanf("%d",&s);
		scanf("%s",str);
		for(i=0;i<=s;i++)
		{
			a[i]=(int)str[i]-'0';
 
		}
			for(i=0;i<=s;i++)
		{
		//cout<<a[i]<<endl;
 
		}
		count=a[0];
		for(i=1;i<=s;i++)
		{
		
			if(i>count && a[i]!=0)
			{
				min=min+i-count;
				count=count+i-count+a[i];
			//	cout<<"enetrer=d else"<<i<<endl;
			}
			else
			count=count+a[i];
			//cout<<count<<"  "<<min<<endl;
		}
		printf("Case #%d: %d\n",k,min);
		k++;
	}
	
	
	return 0;
}
