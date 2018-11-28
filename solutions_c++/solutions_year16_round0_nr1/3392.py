#include<bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	long n;
	cin>>test;
	int Case=1;
	while(test--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<Case<<": "<<"INSOMNIA\n";
			Case++;
		}
		else
		{
			//cout<<"program is here"<<endl;
			int a[10]={0};
			long tempn=n;
			while(1)
			{
				long temp=n;
				
				while(temp)
				{
					//cout<<"program is here temp "<<temp<<endl;

					if(a[temp%10]==0)
					{
						a[temp%10]=1;
					}
					temp/=10;
				}

				if(a[0]==1 && a[1]==1 && a[2]==1 && a[3]==1 && a[4]==1 && a[5]==1 && a[6]==1 && a[7]==1 && a[8]==1 && a[9]==1)
				{
					//cout<<"program is here n "<<n<<endl;
					cout<<"Case #"<<Case<<": "<<n<<endl;
					Case++;
					break;
				}
				n+=tempn;;
			}
		}
	}
	return 0;
}
