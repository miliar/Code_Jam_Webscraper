#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <math.h>

using namespace std;


// converts a given number of base  to base 10
long long int convbase(long long int m,long long int r){
	long long int out=0;
	long long int pp=1;
	long long int rem;
	while(m>0){
		rem=m%10;
		out+=pp*rem;
		pp=pp*r;
		m=m/10;
	}
	return out;
}

long long int isprime(long long int n){
	long long int y=sqrt(n);
	if(n==2)
		return -1;
	for (long long int i = 3; i <= y; i+=2)
	{
		if(n%i==0)
			return i;
	}
	return -1;
}

long long int caldiv(long long int n1, long long int base){
	// this function returns a divisor of the given number.
	long long int num=convbase(n1,base);
	long long int aa = isprime(num);
	return aa;
}

long long int gennextbin(long long int n){
	// cout<<n<<" inside gennextbit"<<endl;
	long long int m=n;
	long long int p,q=1,r;

	while(1){
		p=m%10;
		if(p==0){
			return n+q;
		}
		n=n-q;
		q=q*10;
		m=m/10;
	}
}


 int main( int argc, char const *argv[])
{
	long long int N,n,j,d,x;
	cin>>N>>d>>j;
	long long int base=1;	
	long long int store[12];
	for (long long int i = 0; i < d-2; ++i)
	{
		base=base*10;
	}
	bool bb;
	base=base*10+1;
	// cout<<base<<" sdedfdfdfd"<<endl;
	printf("Case #1:\n");
	long long int count=0;
	while(1){
		bb=0;
		if(count==j)
			break;
		for (long long int i = 2; i <= 10; i++)
		{
			x=caldiv(base,i);
			if(x!=-1){
				store[i]=x;
			}
			else{
				bb=1;
				break;
			}
		}
		if(!bb){
			cout<<base<<" ";
			for (long long int i = 2; i <= 10; i++)
			{
				cout<<store[i]<<" ";
			}
			cout<<endl;
			count++;

		}
		base = gennextbin(base);
		base = gennextbin(base);
	}
	return 0;
}
