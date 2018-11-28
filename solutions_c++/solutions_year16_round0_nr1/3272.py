#include <iostream>
using namespace std;
int main() {
	// your code goes here
	int t,r=1;
	long long int mp;
	cin>>t;
	while(r<=t)
	{
		int hash[10]={0};
		cin>>mp;
		long long int m=mp,tmp=0;
		int flag=1,i=1;
		while(flag&&i<=100)
		{
			flag=0;
			tmp+=mp;
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
			m=mp+tmp;
		}
		 if(i<=100)
		cout<<"Case #"<<r<<": "<<tmp<<"\n";
		 else
	    cout<<"Case #"<<r<<": INSOMNIA"<<"\n";
	    r++;
	}
	return 0;
}
