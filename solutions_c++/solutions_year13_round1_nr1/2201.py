#include<iostream>
//#include<vector>
using namespace std;

int main()
{
	freopen ("A-small-attempt0 (3).in","r",stdin);
	freopen ("fout.in","w",stdout);
	unsigned long long int i,t,r,n,sum;
	
	cin>>t;
for(int j=1;j<=t;j++)
{	sum=0;
	cin>>r>>n;
	for(i=r;;i+=2)
	{	
		sum=sum+2*i+1;
		if(sum>n) break;
	}
	cout<<"Case #"<<j<<": ";
	cout<<(i-r)/2<<endl;
	
}
return 0;
}
