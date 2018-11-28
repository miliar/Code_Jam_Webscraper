#include <iostream>
using namespace std;
int main() {
	// your code goes here
	int t,r=1;
	long long int n;
	cin>>t;
	while(r<=t)
	{
		int hash[10]={0};
		cin>>n;
		long long int m=n,temp=0;
		int flag=1,i=1;
		while(flag&&i<=100)
		{
			flag=0;
			temp+=n;
			while(m>0)
			{
				int x=m%10;
				m/=10;
				hash[x]=1;
			}
			for(int j=0;j<10;j++)
			{
				if(hash[j]!=1)
				{
					flag=1;break;
				}
			}
			i++;
			m=n+temp;
		}
		 if(i<=100)
		cout<<"Case #"<<r<<": "<<temp<<"\n";
		 else
	    cout<<"Case #"<<r<<": INSOMNIA"<<"\n";
	    r++;
	}
	return 0;
}
