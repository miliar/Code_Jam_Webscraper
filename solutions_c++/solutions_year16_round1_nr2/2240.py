#include <iostream>
#include <cstring>
using namespace std;
int main() 
{
	long long int t,i,n,h[3000],k,x,j;
	cin>>t;
	for(i=0;i<t;i++)
	{
		for(k=0;k<3000;k++)
		{
				h[k]=0;
		}
		cin>>n;
		for(j=0;j<2*n-1;j++)
		{
			for(k=0;k<n;k++)
			{
				cin>>x;
				h[x]++;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for(k=0;k<3000;k++)
		{
			if(h[k]%2==1)
				cout<<k<<" ";
		}
		cout<<endl;
	}
	return 0;
}