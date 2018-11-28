#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	long long int t;
	cin>>t;
	long long int ii=1;
	while(t--)
	{
		long long int n;
		cin>>n;
		//cout<<n<<endl;
		int a[10]={0};
		long long int s=n;
		if(n==0)
		{
			cout<<"Case #"<<ii++<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int x=10;
		while(true)
		{
			long long int s2=s;
			//cout<<s<<endl;
			while(s2!=0)
			{
				long long int d=s2%10;
				if(a[d]==0)
				{
					a[d]=1;
					x--;
				}
				s2/=10;
			}
			if(x<=0)
				{
					cout<<"Case #"<<ii++<<": "<<s<<endl;
					break;
				}
			s+=n;
		}

	}
	return 0;
}