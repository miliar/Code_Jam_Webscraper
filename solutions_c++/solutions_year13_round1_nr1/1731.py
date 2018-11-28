#include<iostream>
using namespace std;
int main()
{
	int i,j,n,c[6000];
	long long r,t,tmp;
	cin>>n;
	for(i=0;i<n;i++)
	{
		j=1;
		cin>>r>>t;
		tmp=r;
		tmp=tmp+r+1;
		while(tmp<=t)
		{
			c[i]++;
			tmp=tmp+(r+2*j)+(r+2*j+1);
			j++;
		}
	}
	for(i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": "<<c[i]<<endl;
	}
	return 0;
}
