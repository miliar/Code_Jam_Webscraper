#include<iostream>
#include<cstring>
using namespace std;
typedef unsigned long long ull;

bool readAllDigits(ull n,char *digits,int &count)
{
	int rem;
	while( n != 0)
	{
		rem = n%10;
		if( digits[rem] != 1)
		{
			digits[rem] = 1;
			++count;
		}
		n/=10;
	}
	return count==10?true:false;	
}

int main()
{
	ull n,tmp;
	int count,incr,t,i=1;
	char digits[10];
	cin>>t;
	while(t--)
	{
		cin>>n;
		cout<<"Case #"<<i<<": ";
		if ( n == 0)
		{
			cout<<"INSOMNIA"<<endl;
			i++;
			continue;
		}
		memset(digits,0,10);
		count = 0;
		incr=2;
		tmp = n;
		while(!readAllDigits(n,digits,count))
		{
			n=tmp*incr;
			++incr;
		}
		cout<<n<<endl;
		++i;
	}
	return 0;
}
