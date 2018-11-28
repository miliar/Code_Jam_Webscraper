#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main() {
	// your code goes here
	int t,test=1;
	scanf("%d",&t);
	while(t--)
	{
		long long int x,temp=8,count=0,ans ,j=1;
		scanf("%lld",&x);
		temp=x;
		if(x==0)
		{
			printf("Case #%d: INSOMNIA\n",test++);
			continue;
		}
		int  *arr;
		arr=(int*) calloc (10,sizeof(int));
		
		while(count<10)
		{
		
			x=temp*(j++);
			ans=x;//	cout<<x<<endl;
			while(x)
			{
			//	cout<<x<<endl;
				if(!arr[x%10]){ count++;
				arr[x%10]=1;}
				x=x/10;
			}
		}
		printf("Case #%d: %lld\n",test++,ans);
	}
	return 0;
}
