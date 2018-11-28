#include <iostream>
#include <cstdio>
using namespace std;
long long int D[1000000];
#define gc getchar
void scan(int &x)
{
int flag=0;
register int c = gc();
if(c == '-') flag=1;
x = 0;
for(;(c<48 || c>57);c = gc());
for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
if(flag == 1)x=-x;
}
long long int reverse_int(long long int a)
{
    long long int new_num = 0;
    while(a > 0)
    {
            new_num = new_num*10 + (a % 10);
            a = a/10;
    }
    return new_num;
}
void preprocessing()
{
	for(long long int i = 1; i<=1000000;i++)
	{
		D[i] = -1;
	}
	D[1] = 1;
	for(long long int i= 2; i<=1000000;i++)
	{
		long long int min = 0;
		long long int m = reverse_int(i);
		if(D[m]!= -1 && D[m]<D[i-1] && i%10 != 0 )
		{
			min = D[m]+1;
		}
		else min = D[i-1]+1;
		D[i] = min;
	}
}
main()
{
	int t;
	long long int n;
	scan(t);
	preprocessing();
	for(int k =1;k<=t; k++)
	{
		scanf("%lld",&n);
		printf("Case #%d: %lld\n",k,D[n]);
	}
}
