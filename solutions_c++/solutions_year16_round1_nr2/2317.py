#include<iostream>
using namespace std;
int main()
{
	int t,x,i,temp;
	cin>>t;
	for(x=1; x<=t; x++)
	{
		int n,a[2501]={0};
		cin>>n;
		int lim=((2*n)-1)*n;
		for(i=0; i<lim; i++)
		{
			cin>>temp;
			a[temp]++;
		}
		cout<<"Case #"<<x<<": ";
		for(i=0; i<=2500; i++)
		{
			if(a[i]%2!=0)
			{
				cout<<i<<" ";
			}
		}
		cout<<"\n";
	}
}
