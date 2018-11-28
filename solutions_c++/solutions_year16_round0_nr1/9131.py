#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int last,a[10]={0},temp,j=2,flag=false;
		long long int n,h;
		cin>>n;
		h=n;
		while(flag==false)
		{
			if(n==0)
			{
				flag=true;
				break;
			}
			temp=h;
			while(temp>0)
			{
				last=temp%10;
				a[last]++;
				temp=temp/10;
			}
			for(int i=0;i<10;i++)
		{
			if(a[i]==0)
			break;
			else if(a[i]>0&&i==9)
			{
				flag=true;
				n=h;
				break;
			}
		}
			if(flag==false)
			{
			h=n*j;
			j++;
			}
		}
		if(flag==true&&n!=0)
		printf("Case #%d: %lld\n",k,n);
		else if (flag==true&&n==0)
		printf("Case #%d: INSOMNIA\n",k);
	}
}
