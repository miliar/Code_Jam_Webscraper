#include <fstream>
#include <string>
#include <algorithm>

//get a mutiplier of 10.
std::string get_a_bound( int front, int digit );

//get product
std::string get_square_product( std::string a );

//check if is palindrome.
bool is_palin( std::string a);

//increase by 1 and keeping it palidorme.
bool get_next( std::string & a );

bool is_bigger( std::string a, std::string b );


int main()
{

	//open files.
	std::ifstream in;
	std::ofstream out;

	in.open("C-small-attempt0.in");
	out.open("C-small-attempt0.out");

	//global variables.
	int T, count;
	std::string A, B, L, U, number;

	//in and out.
	in >> T;
	for( int t = 0; t < T; t ++ )
	{
		in >> A >> B;

		count = 0;

		//get lower boundary and upper boundary.
		L = get_a_bound( 1, ( A.length() - 1 )/2 );

		//get upper boundary.
		U = get_a_bound( 4, ( B.length() - 1 )/2 );

		//only restrctions in U's length.
		for( int len = L.length(); len <= U.length(); len ++ )
		{
			number.clear();

			for( int digit = 0; digit < len; digit ++ )
			{
				number += '0';
			}

			if( number.length() != 1 )
			{
				number[0] = '1';
				number[number.length() - 1] = '1';
			}

			std::string product;
			while( 1 )
			{
				if( is_palin( number ) )
				{
					product = get_square_product(number);

					if( is_bigger( product, B ) )
					{
						break;
					}

					if( !is_bigger( A, product ) && is_palin(product) )
					{
						count ++;
					}
				}

				if( ! get_next( number ) )
				{
					break;
				}

			}
		}

		out << "Case #" << t + 1 << ": " << count << std::endl; 

		//clear memeory.
		number.clear();


	}

	//close files.
	in.close();
	out.close();

	return 0;
}


std::string get_a_bound( int front, int digit )
{
	std::string result;
	result = ( char )(front + 48);
	
	//append 0s.
	for( int i = 0; i < digit; i ++ )
	{
		result += '0';
	}

	return result;
}

std::string get_square_product( std::string a )
{
	std::string product;

	for( int i = 0; i < a.length(); i ++ )
	{
		product += "00";
	}

	product += "0";

	//the result is swapped.
	for( int i = a.length() - 1; i >= 0; i -- )
	{
		for( int j = a.length() - 1; j >= 0; j -- )
		{
			int p = ( a[i] - 48 ) * ( a[j] - 48 );

			int o = ( product[ 2 * a.length() - i - j ] - 48 ) * 100 + 
				( product[ 2 * a.length() - i - j - 1 ] - 48 ) * 10 + 
				( product[ 2 * a.length() - i - j - 2 ] - 48 );

			//original add temp product.
			o = o + p;

			product[ 2 * a.length() - i - j ] = ( o / 100 + 48 );
			o = o % 100;

			product[ 2 * a.length() - i - j - 1 ] = ( o /10 + 48 );

			product[ 2 * a.length() - i - j - 2 ] = ( o % 10 + 48 );


		}
	}

	//get rid of 0s.
	for( int i = product.length() - 1; i > 0; i -- )
	{
		if( product.back() == '0' )
		{
			product.pop_back();
		}
	}

	std::reverse( product.begin(), product.end() );

	return product;
}


bool is_palin( std::string a )
{
	for( int i = 0; i <= a.length()/2; i ++ )
	{
		if( a[i] != a[ a.length() - i - 1 ] )
		{
			return false;
		}
	}

	return true;
}

bool get_next( std::string & a )
{

	if( a.length() == 1 )
	{
		if( a[0] == '9' )
		{
			return false;
		}
		a[0] ++;
		return true;
	}

	if( a.length() == 2 )
	{
		if( a[0] == '9' )
		{
			return false;
		}
		a[1] ++;
		a[0] = a[1];

		return true;
	}

	for( int i = a.length()/2; i <= a.length() - 1; i ++ )
	{
		if( a[ i ] != '9' )
		{
			a[ i ]++;
			a[a.length() - i - 1] = a[ i ];

			return true;
		}else
		{
			a[ i ] = '0';
			a[a.length() - i - 1] = a[ i ];
		}

		
	}

	return false;
}

bool is_bigger( std::string a, std::string b )
{
	if( a.length() > b.length() )
	{
		return true;
	}

	if( b.length() > a.length() )
	{
		return false;
	}

	for( int i = 0; i < a.length(); i ++ )
	{
		if( a[i] > b[i] )
		{
			return true;
		}

		if( a[i] < b[i] )
		{
			return false;
		}
	}

	return false;

}