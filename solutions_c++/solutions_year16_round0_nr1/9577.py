#include<iostream>
#include<stdio.h>

using namespace std;
bool check(int a[])
{

	if((a[0]>0)&&(a[1]>0)&&(a[2]>0)&&(a[3]>0)&&(a[4]>0)&&(a[5]>0)&&(a[6]>0)&&(a[7]>0)&&(a[8]>0)&&(a[9]>0))
	{
		return true;
	}
	else return false;
}
int main()
{
	int t;
	int n;
	scanf("%d",&t);
	for(int k=0;k<t;k++)
	{
		int i=1;
		scanf("%d",&n);
		int a[10]={0};
		if(n!=0)
		{
			int nn=n;
			while(check(a)==false)
			{
				int temp=nn;
				while(temp>0)
				{
					++a[temp%10];
					temp/=10;
				}
				nn=n*i;
				++i;
			}
			printf("Case #%d: %d\n",k+1,n*(i-2));
		}
		else printf("Case #%d: INSOMNIA\n",k+1);
	}
	return 0;
}
