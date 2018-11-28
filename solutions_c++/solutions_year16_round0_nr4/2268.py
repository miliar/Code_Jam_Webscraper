#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	long t,k,c,s;
	cin>>t;
	for(long i=0;i<t;i++)
	{
		cin>>k>>c>>s;
		if(k==s)
		{
			cout<<"Case #"<<i+1<<": ";	
			for(long j=0;j<k;j++)
			{
				cout<<j+1<<" ";
			}
			cout<<endl;
	    }
	}
	return 0;
}
