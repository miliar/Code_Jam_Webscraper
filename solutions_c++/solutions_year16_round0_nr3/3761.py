#include<iostream>
#include<math.h>
using namespace std;

long setn = 16 ;
long setj = 50 ;
long count = 0;
long long ans[11] ; 



int increment(char a[])
{
	for(long i=setn-2 ; i>0 ; i--)
	{
		if(a[i] == '0')
		{
			a[i] = '1';
			break;
		}
		else 
		{
			a[i] = '0';
		}
	}
	
}

long long power(long long base , long long exp)
{
	long long pow = 1;
	
	while(exp > 0)
	{
		if(exp%2 == 1)
		{
			exp--;
			pow*=base;
		}
		base*=base;
		exp /= 2;
	}
	
	return pow;
}

long long baseval(char a[] , int base)
{
	
	long long sum = 0;
	for(long long i=0;i<setn;i++)
	{
		if(a[i] == '1')
		sum+= power(base,setn-i-1);
	}
	return sum;
}


long long check(long long n)
{
	long long i;
	for(i=3;i<=sqrt(n);i++)
	{
		if(n % i == 0)
		return i;
	}
	
	return 1;
}




int main()
{
	char a[40]="1";
	long i;
	for(i=1;i<setn-1;i++)
	a[i] = '0';
	a[i++] = '1';
	cout<<"Case #1: \n";
	//cout<<power(2,3);
	
	long long x,y,z;
	cin>>x>>y>>z;
	
	while(count != setj)
	{
		long status = 1;
		
		for(i=2;i<=10;i++)
		{
			long long temp = check(baseval(a,i));
			
			if (temp == 1)
			{
				status = 0;
				break;
			}
			
			ans[i] = temp ;
			
		}
		
		if(status)
		{
			cout<<a;
			for(i=2;i<=10;i++)
			cout<<" "<<ans[i] ;
			
			cout<<endl ;
			count++ ;
		}
		
		increment(a);
	}
	
}
