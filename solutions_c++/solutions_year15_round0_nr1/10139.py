#include <iostream>
using namespace std;

int main() 
{
	long t, n, smax, i, sum, k, temp;
	char str[1000];
	cin>>t;
	for(k=1; k<=t; ++k)
	{
		cin>>smax;
		cin>>str;
		sum=n=0;
		for(i=0; i<=smax; ++i)
		{
			temp=i-sum;
			if(temp>0)
			{
				n+=temp;
				sum+=temp;
			}
			sum+=(str[i]-'0');
		}
		cout<<"Case #"<<k<<": "<<n<<"\n";
	}
	return 0;
}