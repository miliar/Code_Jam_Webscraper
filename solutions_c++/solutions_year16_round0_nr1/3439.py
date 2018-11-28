#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		int c=0;
		bool vis[10]={0};
		long long int num=0,temp,k;
		bool flag=0;int ii=1;
		cin>>num;temp=num;
		if(num==0)
			cout<<"INSOMNIA\n";
		else
		{

			while(true)
			{
				k=temp;
				while(temp!=0)
				{
					int r=temp%10;
					//cout<<r<<" ";
					if(!vis[r])
					{
						vis[r]=1;
						c++;
						if(c==10)
						{
							flag=1;
							cout<<k<<"\n";
							break;
						}
					}
					temp=temp/10;
				}
				//cout<<"\n";
				ii++;
				temp=num*ii;
				if(flag)
					break;
			}
		}
	}
	return 0;
	



}