#include <iostream>
using namespace std;
int work();
int main() 
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": "<<work()<<endl;
	}
	return 0;
}

int work()
{
	int ctr=0,a,b,k,i,j;
	cin>>a>>b>>k;
	for(i=0;i<a;i++)
	{
		for(j=0;j<b;j++)
		{
			if((i&j)<k)
			{
				ctr++;
			}
		}
	}
	return ctr;
}