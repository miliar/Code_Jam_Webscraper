#include <iostream>
#include <cstring>
#include <bitset>
#include <vector>
using namespace std;

vector<int> primes;
int count;
unsigned long int divisible[10];

unsigned long long int tonumber(bitset<16> k, int n, int base)
{
	unsigned long long int num=0;
	for(int i=(n-1);i>=0;i--)
	{
		num=num*base + k[i];
	}
	return num;
}

int function3(bitset<16> k, int n, int base, int p)
{
	int x=0;
	for(int i=n-1;i>=0;i--)
		x=(x*base + k[i])%p;
	return (x==0);
}

void function2(bitset<16> k, int n, int j)
{
	int f;
	int c=0;
	unsigned long int temp;
	for(int i=2;i<=10;i++)
	{
		f=0;
		temp=tonumber(k,n,i);
		for(unsigned long int m=2; m*m<=temp;m++)
		{
			if(primes[m])
			{
				if(function3(k,n,i,m))
				{
					divisible[i]=m;
					f=1;
					break;
				}
				if(f==1)
					break;
			}
			if(f==1)
				break;
		}
		if(f==0)
			return;
		else
			c=c+1;
	}
	if(c==9)
	{
		count=count+1;
		for(int i=n-1;i>=0;i--)
			cout<<k[i];
		cout<<" ";
		for(int i=2;i<=10;i++)
			cout<<divisible[i]<<" ";
		cout<<endl;
	}
}

void startingprime()
{	
	for(unsigned long int i=0;i<=110000000;i++)
		primes.push_back(1);
	primes[0] = false;
    primes[1] = false;
    for (unsigned long int i = 2; i <= 110000000; ++i)
    {
    	if (primes[i])
    	{
    		 for (unsigned long int j = i + i; j <= 110000000; j += i)
    		 	primes[j] = false;
    	}
    }
}

void generatenum(int x, bitset<16> k, int n,int j)
{
	for(int i=0;i<n-2;i++)
		k[i+1]=(x>>i)&1;

	if((x>>(n-2)) !=0) return;
	else
	{
		function2(k,n,j);
		if(count==j)
			return;
		generatenum(x+1,k,n,j);
	}
}

void function1(int n, int j)
{
	bitset<16> num;
	num |=1;
	num=num<<(n-1);
	num |=1;
	generatenum(0,num,n,j);
}

int main()
{
	startingprime();
	int t,j,i,n;
	cin>>t;
	for(i=0;i<t;i++)
	{
		count=0;
		cin>>n;
		cin>>j;
		cout<<"Case #"<<(i+1)<<":"<<endl;
		function1(n,j);
	}
	return 0;
}