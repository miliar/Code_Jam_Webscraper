#include<iostream>
using namespace std;
int main()
{
	int t,a,b,n,k,count;
	cin>>t;
	int l=t;
	while(t--)
	{
		count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int c=0;c<b;c++)
			{
				n=(i&c);
				if(k>n)count++;
			}
		}
		cout<<"Case #"<<(l-t)<<": ";
		cout<<count<<"\n";
	}
	return 0;
}

