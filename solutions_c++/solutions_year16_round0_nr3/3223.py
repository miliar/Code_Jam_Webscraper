#define _USE_MATH_DEFINES
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

void next(char B[], int n)
{
	int i;
	for(i=n-2;i>0;i--)
	{
		if(B[i]=='1')
			B[i]='0';
		else
		{
			B[i]='1';
			break;
		}
	}
}

unsigned long long int factor(unsigned long long int n)
{
	unsigned long long int i;
	for(i=2;i<sqrt(n);i++)
	{
		if(n%i==0)
			return i;
	}
	return 0;
}

unsigned long long int convert(char B[], int n, int b)
{
	unsigned long long int s=0;
	int i;
	for(i=0;i<n;i++)
	{
		s+=pow(b,i)*(B[n-i-1]-'0');
	}
	return s;
}

int main()
{
    unsigned int t,i,n,j,k,count;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    	cin>>n>>j;
    	cout<<"Case #"<<i<<":\n";
    	char B[n];
    	B[0]='1';
    	B[n-1]='1';
    	for(k=1;k<n-1;k++)
    		B[k]='0';
    	count=0;
    	unsigned long long int number, fact[9];
    	while(count!=j)
    	{
    		bool check=true;
    		for(k=2;k<=10;k++)
    		{
    			number=convert(B,n,k);
    			fact[k-2]=factor(number);
    			if(!fact[k-2])
    			{
    				check=false;
    				break;
    			}
    		}
    		if(check)
    		{
    			for(k=0;k<n;k++)
    				cout<<B[k];
    			for(k=2;k<=10;k++)
    				cout<<" "<<fact[k-2];
    			cout<<endl;
    			count++;
    		}
    		next(B,n);
    	}
    }
    return 0;
}
