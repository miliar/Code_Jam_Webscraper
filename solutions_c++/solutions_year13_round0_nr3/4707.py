#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	 //freopen("C.in","r",stdin);
     //freopen("outputC.in","w",stdout);

	int t;
	cin>>t;
	int x=1;
	long long a1[50]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111,20000002,100000001};
	long long b1[50];
	for(int i=0;i<50;i++)
		{
			b1[i]=a1[i]*a1[i];
		}
	while(t--)
	{
		int count=0;
		long long a,b;
		cin>>a>>b;
		for(int i=0;i<50;i++)
		{
			if(b1[i]>=a&&b1[i]<=b)
			{
				count++;
			}
			else if(b1[i]>b)
				break;
		}
		cout<<"Case #"<<x<<": "<<count<<endl;
		x++;
	}
}
