#include <cstdio>
#include <string>
#include <iostream>
#include <bitset>
#include <vector>
#include <cmath>
#include <sstream>
#include <cassert>
using namespace std;

bool isprime(unsigned long long int n)
{
	if(n<=1) return false;
	if(n==2) return true;
	if(n%2==0) return false;
	int m=int(sqrt((float)n));

	for(int i=3;i<=m;i+=2)
	{
		if (n%i==0) return false;
	}
	return true;
}

unsigned long long factor(unsigned long long int n)
{
	unsigned long long i = 1;
	for ( ; i * i < n; i++ )
	{
		if ( n % i == 0 )
		{
		    if ( ( i != 1 ) && ( i != n ) )
		    {
		        return i;
		    }
		    if ( ( (n / i) != 1 ) && ( ( n / i ) != n ) )
		    {
		        return n / i;
		    }
		}
	}	
	if ( n == i * i )
	{
	    if ( ( i != 1 ) && ( i != n ) )
	    {
	        return i;
	    }
	}
	assert( false );
	return 0;
}

int main()
{
#ifdef DEBUG_ONLINE_JUDGE
    FILE* out = NULL;
    FILE* in = NULL;
    char* filenameOut = "out.txt";
    char* filenameIn = "in.txt";
    freopen_s( &out, filenameOut, "w", stdout );
    freopen_s( &in, filenameIn, "r", stdin );
#endif
    int T = 0;
    scanf( "%d", &T );
    int N = 0;
    int J = 0;
    scanf( "%d %d", &N, &J );
    puts( "Case #1:" );
    int firstNumber = (1<<N)+1;
    while( true )
    {
        bitset<16> bs(firstNumber);
        if ( !bs.test( 0 ) || !bs.test( N - 1 ) )
        {
            firstNumber++;
            continue;
        }
        unsigned long long number = 0;
        bool okNumber = true;
        vector< unsigned long long > numbers;
        for ( int base = 2; base <= 10; ++base )
        {
            unsigned long long potBase = 1;
            number = 0;
            for ( int i = 0; i < N; ++i )
            {
                if ( bs.test( i ) )
                {
                    number += potBase;
                }
                potBase *= base;
            }
            if ( isprime( number ) )
            {
                //cout<<"error "<<bs<<endl;
                okNumber = false;
                break;
            }
            numbers.push_back( number );
        }
        if ( okNumber )
        {
            string ss = bs.to_string();
            for ( int i = 0; i < numbers.size(); ++i )
            {
                unsigned long long someFactor = factor( numbers[i] );
                ss += " ";
                stringstream in;
                in << someFactor;
                string temp;
                in >> temp;
                ss += temp;
            }
            cout<<ss<<endl;
            --J;
            if ( J == 0 )
            {
                break;
            }
        }
        firstNumber++;
    }
}

