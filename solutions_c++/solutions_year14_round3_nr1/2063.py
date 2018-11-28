#include <iostream>
#include <algorithm>
#include <string>
#include <stdlib.h>
using namespace std;
string input;
long long p, q;

long long GCD(long long a, long long b)
{
	long long c; 
	while ( a != 0 ) 
	{ c = a; a = b%a; b = c; } 
	return b; 
}

void gen(long long p, long long q, int x)
{
	long long gcd;
	gcd=GCD(q,p);
	p=p/gcd;
	q=q/gcd;
	
	long long pow=q;
	while(pow>1)
	{
		if(pow%2!=0)
		{
			cout << "Case #" << x << ": impossible" << endl;
			return;
		}
		pow=pow>>1;
	}
	int z = 1;
	while(p*2 < q)
	{
		q=q>>1;
		z++;
	}
	cout <<"Case #" << x << ": " << z << endl;
}

void fun(int j)
{   
	cin >> input;
    
	string::size_type divider = input.find_first_of("/", 0);
	p = atoi(input.substr(0, divider).c_str());
	q = atoi(input.substr(divider+1, input.length()).c_str());
	gen(p,q,j);
}



int main()
{
	int i;
	cin >> i;
	for (int j=1; j<=i; j++)
	{
		fun(j);
	}
	
	return 0;
	
}
