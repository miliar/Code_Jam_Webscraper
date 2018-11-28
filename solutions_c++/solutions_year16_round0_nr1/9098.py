#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,n,n1,n2,t1;
	cin>>t;
	t1=t;
	while(t!=0)
	{   
		int a[10];
		for(int i=0;i<10;i++)
		{
			a[i]=0;
		}
		cin>>n;
		cout<<"case #"<<t1-t+1<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{   n1=0;
		    n2=n;
			int temp=0;
			while(temp==0)
			{
				n1+=n;
				n2=n1;
				while(n2!=0)
				{
					int tep=n2%10;
					if(a[tep]==0)
					{
						a[tep]++;
					}
					n2=n2/10;
				}
				int sum=0;
				for(int i=0;i<10;i++)
				{
					sum+=a[i];
				}
				if(sum==10)
				{
					cout<<n1<<endl;
					temp++;
				}
			}
			
		}
		t--;
	}
}
