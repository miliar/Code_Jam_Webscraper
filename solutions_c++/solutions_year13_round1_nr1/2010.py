#include<iostream>
#include<cstdio>
using namespace std;


int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin>>t;
	int q=0;
	while(t--)
	{
		q++;
		long long int r,m;
		cin>>r>>m;
		long long int sum=0;
		long long int x,y;
		x=r+1;
		while(r>0)
		{
			long long int p=x*x-r*r;
			if(m-p>=0)
			{
				sum=sum+1;
				m=m-p;
				r=r+2;
				x=x+2;
			}
			else
			break;
			
		}
		cout<<"Case #"<<q<<": "<<sum<<endl;
	}
}
