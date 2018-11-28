//#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<cstring>
#include<set>

using namespace std;

long long tab[505];
long long divi[505][11];
const int Nlen=16;


long long change(int n, int base)
{
	long long X =0;
	long long Curr=1LL;
	for( int i=0; i< Nlen; ++i)
	{
		if( n&(1LL<<i) ) X+=Curr;
		Curr*=base;
	}
	return X;
}

bool prime(long long X, int pos, int base)
{
	for( long  long i=2; i*i<=X; ++i)
		if( X % i ==0)
		{
			divi[pos][base]=i;
			return 0;
		}
	return 1;
}

bool OK(int n, int pos)
{
	for(int i=2; i<=10; ++i)
	{
		long long X = change(n, i);
		if( prime( X , pos, i) )return 0;
	}
	return 1;
}


void pre(int J)
{
	for( int i = (1LL<<(Nlen-1))+1, j=0;
		 j< J and i < (1LL<<Nlen); i+=2)
		if(OK(i,j))
		{
			tab[j] = i;
			j++;
		}
			
}

void print(long long  X)
{
	for(int i=Nlen-1; i>-1; i--)
		if(X&(1LL<<i)) putchar('1');
		else putchar('0');
	printf(" ");

}

int main()
{
	pre(50);
	
	printf("Case #1:\n");
	
	for(int i=0; i<50; ++i)
	{
		print(tab[i]);
		//printf( "err: %lld\n", change(tab[i],6));
		for( int j=2;j<=10; ++j)
			printf("%lld ", divi[i][j]);
		printf("\n");
	}
	
	return 0;
}
