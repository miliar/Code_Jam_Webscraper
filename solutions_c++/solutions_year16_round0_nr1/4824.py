#include <iostream>

void func(long long int a0);
//calculates which digits are there in a0 and changes the array a

bool check();
//returns false if all the digits have appeared once

long long int a[10]={};//a[i] stores the number of times i has occured

int main()
{
	int t=0;
	long long int n=0,j=0;
	std::cin>>t;
	for(int i=1;i<=t;++i)
	{
		std::cin>>n;
		if(n!=0)
		{
			for(j=1;check();++j)
			{
				func(j*n);
			}
		    std::cout<<"Case #"<<i<<":  "<<((j-1)*n)<<"\n";	
		}
		else
		{
			std::cout<<"Case #"<<i<<":  INSOMNIA\n";
		}
		for(int i0=0;i0<=9;++i0)
		{
			a[i0]=0;
		}
	}
	return 0;
}

void func(long long int a0)
{
	while(a0!=0)
	{
		++a[a0%10];
		a0/=10;
	}
}

bool check()
{
	bool flag=false;
	for(int i=0;i<=9;++i)
	{
		if(a[i]==0)
		{
			flag=true;
			break;
		}
		else
		{
			;
		}
	}
	return flag;
}