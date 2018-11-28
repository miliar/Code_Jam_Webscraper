#include<iostream>
using namespace std;
#include<stdio.h>
int main(){
	int t,a,b,k,i,j,inc=1,x;
	long long count;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&a,&b,&k);
		count=0;
		for(i=a-1 ; i>=0 ; i--)
		{
			for(j=b-1 ; j>=0 ; j--)
			{
				x=i&j;
				if(x<k)
				count++;
			}
		}
		printf("Case #%d: %lld\n",inc++,count);
	}
	return 0;
}
