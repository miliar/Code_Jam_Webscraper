#include <iostream>
#include <math.h>

using namespace std;

long long squareP [40]={0};


int palindrome(long long i)
{
	long long n, n1, rev = 0, rem;
	n=i;
	n1 = n;
	/* logic */
	while (n > 0){
	rem = n % 10;
	rev = rev * 10 + rem;
	n = n / 10; }
	if (n1 == rev)
	{
		//cout<<n1<<endl;
		//printf(" Given number is a palindromic number\n");
		return 1;
	}
	else
	{
		//printf("Given number is not a palindromic number");
		return 0;
	}
}

int main()
{
	int t=0;
	long long ll =0;
	int count=0;
	int ctr=0;
	ll = (long long)pow(10,14);

	cin>>t;

	for(long long j =10000000; j>=1 ;) //&& j*j <=b; )
	{
		if(palindrome(j) == 1)
		{
			if(palindrome(j*j) == 1)
			{
				//cout<<j<<" ... "<<(j*j)<<endl;
				squareP[ctr]=(j*j);
				ctr++;
			}
		}
		j--;
	}
	//cout<<"Found fair and square "<<ctr<<endl;
	ctr=0;

	for (int i=1; i <=t; i++)
	{
		long long a=0;
		long long b=0;
		long ctr=0;

		cin>>a;
		cin>>b;


		cout<<"Case #"<<i<<": ";

		{
			for(int x=0; x<40;x++)
			{
				if( squareP[x] >= a && squareP[x] <=b )
					ctr++;
			}

		}
		cout<<ctr<<endl;


	}
	return 0;
}
