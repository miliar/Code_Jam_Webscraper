#include<bits/stdc++.h>
using namespace std;
#define LL long long
int main()
{
	FILE *ap,*op;
	ap=fopen("A-large.in","rt");
	op=fopen("output.txt","wt");
	int t;
	fscanf(ap,"%d",&t);
	for(int r=1;r<=t;r++)
	{
		LL n,flag=0;
		fscanf(ap,"%lld",&n);
		int arr[10]={0};
		if(n==0)
			fprintf(op,"Case #%d: INSOMNIA\n",r);
		else
		{
			flag=1;
			
			for(LL i=1;flag;i++)
			{
				int temp=i*n;
				while(temp!=0)
				{
					arr[temp%10]=1;
					temp=temp/10;
					
				}
				flag=0;
				for(int j=0;j<10;j++)
				{
					if(arr[j]!=1)
						flag=1;
				}
				if(flag==0)
					fprintf(op,"Case #%d: %lld\n",r,i*n);
			}
		}
	}
}
