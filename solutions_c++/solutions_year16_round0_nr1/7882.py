#include <iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main() {
	// your code goes here
	int t ;
	scanf("%d",&t);
	//cout<<t;
	for(int j=1;j<=t;j++)
	{
		long int n;
		scanf("%ld",&n);
		long int add=0,check,sum=0;
		int a[10];
		memset (a,0,sizeof(a));
		if(n!=0)
		{
		while(1)
		{
			add+=n;
			check = add;
			while(check>0)
			{
				if(!a[check%10]){
					a[check%10]=1;
					sum+=(check%10);
				}
				check/=10;
			}
			if(sum==45 && a[0]==1)
			{
			printf("Case #%d: %ld\n",j,add);
			break;
			}
		}
		}
		else{
			printf("Case #%d: INSOMNIA\n",j);
		}
	}
	return 0;
}