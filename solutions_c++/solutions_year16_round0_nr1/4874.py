#include <iostream>
using namespace std;

int main() {
	int t,tt,l;
	long n;
	long long ret,p,nn;
	cin>>t;
	tt=t;
	while(tt--)
	{
		int a[]={0,0,0,0,0,0,0,0,0,0};
		cin>>n;
//		n=t-tt-1;cout<<n<<"= ";
		if(n)
		{
			ret=l=0;
			p=1;
			while(l<10)
			{
				nn=ret=n*p;
				p++;
				while(nn)
				{
					if(!a[nn%10]++)
					{	
						l++;
					}
					nn/=10;
				}
			}
			cout<<"Case #"<<t-tt<<": "<<ret<<endl;
		}
		else
			cout<<"Case #"<<t-tt<<": INSOMNIA"<<endl;
	}
	return 0;
}