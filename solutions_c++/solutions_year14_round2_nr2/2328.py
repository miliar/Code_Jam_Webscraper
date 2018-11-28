#include<iostream>
using namespace std;

int calc(int a,int b,int k,int count)
{
	for(int i=0;i<a;i++)
	{
		for(int j=0;j<b;j++)
		{
			if((i&j)<k)
			{
				count++;
			}
		}
	}
	return count;			
}
int main()
{
		int t,a,b,k,x=1;
		cin>>t;
		while(x<=t)
		{
			int count=0;
			cin>>a>>b>>k;
			count=calc(a,b,k,count);
			cout<<"Case #"<<x<<":"<<" "<<count<<"\n";
			x++;
		}
}
