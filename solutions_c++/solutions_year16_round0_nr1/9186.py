#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out3.out","w",stdout);
	int t,i;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
	int a[10]={0};
	int flag;
	long long int n;
	cin>>n;
	if(n==0)
	cout<<"Case #"<<j<<": INSOMNIA"<<endl;
	else
	{
		for(long long int i=1;;i++)
		{
		  long long int m=n*i;
		  flag=0;
		  long long int d=m;
			while(d!=0)
			{
				a[d%10]++;
				d=d/10;
			}
			for(int i=0;i<10;i++)
			{
				if(a[i]==0)
				flag++;
			}
			if(flag==0)
			{
				cout<<"Case #"<<j<<": "<<m<<endl;
				break;
			}
			
		}
	}
}
return 0;	
}

