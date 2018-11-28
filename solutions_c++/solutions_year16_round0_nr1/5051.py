#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int n,nc,flag;
	long long c,k;
	int i,j;
	int a[10]={0,0,0,0,0,0,0,0,0,0};

	
	cin>>n;
	nc=n;
	while(n>0)
	{
		for(i=0;i<10;i++)
			a[i]=0;
		cin>>k;
		
		c=k;
		j=1;
		if(k==0)
		{
			cout<<"Case #"<<(nc-n)+1<<": INSOMNIA\n";
			n--;
			
			continue;
		}
		while(1)
		{
			c=k*j;
			while(c>0)
			{
				a[c%10]=1;
				c/=10;
			}
			flag=1;
			for(i=0;i<10;i++)
			{
				if(a[i]==0)
				{
					flag=0;
					break;
				}
			}
			if(flag) break;
			
			j++;
			
			
		}
		cout<<"Case #"<<(nc-n)+1<<": "<<k*j<<endl;
		n--;
	
		
	}
}
