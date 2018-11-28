#include <vector>
#include <bitset>
#include <iostream>
#include <cmath>
#include <set>

using namespace std;



void make_base( vector<long int> & mybase ,int rads, long int base )
{
	int i = 0;
	long int mul = 1;

	mybase.push_back( 1);
	for( int i = 0; i < rads; i ++ )
	{
		mul = mul * base;
		mybase.push_back( mul );
	}

}

void find_primes( set<long int> & primetree ,int power)
{
	long int i;
	bool add;
	vector<long int> myprimes;
	myprimes.push_back( 2 );
	long int size = 1;
	long int max = pow( 10 , power/2 ) ;
	long int square;

	for( i = 3; i < max; i = i + 2 )
	{
		add = true;

		square = sqrt( i );
		for( int j = 0;  add && myprimes[j] <= square ; j++ )
		{
			if( i % myprimes[j] == 0 )
			{
				add = false;
			}		
			
		}
		if( add)
		{
			myprimes.push_back( i );
		}		

	}

	while( myprimes.size() > 0)
	{
		primetree.insert( myprimes.back() );
		myprimes.pop_back();
	}

}

long int prime_base( int x , vector<long int> base, set<long int> prime )
{
	long int square;
	long int total = 0;
	set<long int>::iterator it;

	for( int i = 0; x > 0 ; i ++ )
	{
		total = total + ( ( ( x ) & 0x1)* base[i] );
		x = x >> 1;
	}

	it = prime.find( total );

	if( it == prime.end() ) 
	{
		square = sqrt( total);
		for ( it = prime.begin(); *it <= square ; it++ )
		{
			if( total % *it == 0 )
			{
				//cout << *it << " devides " << total << endl;
				return *it;
			} 
		}		
		return -1;
	}
	else
	{
		return -1;
	}
	

}

void sieve( vector<bool> primes, int power )
{

	

}

int print_sol ( long int n, vector<long int> div )
{
	//while( n > 0)
	//{
	//	cout << (n & 0x1);
	//	n = n >> 1;
	//}
	cout << std::bitset<16>(n) ;



	for( int i = 0; i < 9; i ++)
	{
		cout << " " << div[i];
	}
	endl( cout );
}


int main ()
{
	int t;
	set<long int> primes;
	vector<long int> base[9];
	vector<long int> div;
	bool flag;
	long int temp;
	int i; // tracker
	int f; //found 
	int j; //ammount to find

	//long int herp = ( 2.0 , 32.0 );

	//vector<bool> test;
	//test.resize( herp, 0 );

	cin >> t;
	cin >> t;
	cin >> j;


	find_primes( primes, t);
	for( i = 2; i <= 10; i++)
	{
		make_base( base[i-2] , t ,  i );
	}

	i = (1 << t-1) + 1;

	cout << "Case #" << 1 << ":\n" ;
	//for( ; i< 0b1000000 ; i+=2)
	for( ; f < j ; i+=2)
	{
		flag = true;
		div.clear();
		for( int k = 0; k < 9 && flag ; k ++)
		{
			temp = prime_base( i , base[k] , primes );
			if( temp == -1 )
			{
				flag = false;	
			}
			else
			{
				div.push_back( temp );
			}
		}	
		if ( flag )
		{
			f++;
			print_sol( i , div );
		}	
	}	
}
