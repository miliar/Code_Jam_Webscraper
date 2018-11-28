#include<iostream>


using namespace std;

long xxx(long a[],long long n)
{
	for(int i=0;i<10;i++)
	{
		cout<<","<<a[i];
	}
	cout<<endl;
	cout<<n<<endl;
}

long check(long a[])
{
	for(int i=0;i<10;i++)
	{
		if(a[i] == 0)
		return 0;
	}
	
	return 1;
}

long k=1;

long keepgoing(long a[] , long long n , long long base)
{
	//xxx(a,n);
	k++;
	long long temp = n;
	while(temp)
	{
		long digit = temp%10;
		a[digit] = 1;
		temp/=10;
	}
	int status = check(a);
	
	if(status == 0)
	{
		return keepgoing(a,base*k,base);
	}
	else
	{
		return n;
	}
	
}

int main()
{
	long t;
	cin>>t;
	long casee =1;
	while(t--)
	{
		long long n;
		cin>>n;
		long a[10] = {0,0,0,0,0,0,0,0,0,0};
		k=1;
		if(n!=0)
		cout<<"Case #"<<casee++<<": "<<keepgoing(a,n,n)<<endl;
		else
		cout<<"Case #"<<casee++<<": "<<"INSOMNIA"<<endl;
		}	
}
