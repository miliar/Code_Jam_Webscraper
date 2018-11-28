#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("p0largeoutput.txt","w",stdout);
	//freopen("p0smalloutput.txt","w",stdout);
	long int n,t,i,arr[10]={0},a,flag,count=0,b,k,j;
	scanf("%ld",&t);
	for(k=1;k<=t;k++)
	{
	    long int arr[10]={0};
		scanf("%ld",&n);
		if(n==0)
			printf("Case #%ld: INSOMNIA\n",k);
		else
		{
		    count=0;
			i=1;
			while(count<10)
			{
				a=n*i;
				b=a;
				while(a>0)
				{
					arr[a%10]++;
					a=a/10;
				}
				count=0;
				for(j=0;j<10;j++)
				{
					if(arr[j]>0)
						count++;
				}
				i++;
			}
			printf("Case #%ld: %ld\n",k,b);
		}
	}
	return 0;
}