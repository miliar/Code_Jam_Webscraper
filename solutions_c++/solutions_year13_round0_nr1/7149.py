//

#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>


enum result
{
	result_x,
	result_o,
	result_draw,
	result_not_completed
};


bool is_x( std::string const & s )
{
	return ( 0 == s.compare( "XXXX" ) )
		|| ( 0 == s.compare( "TXXX" ) )
		|| ( 0 == s.compare( "XTXX" ) )
		|| ( 0 == s.compare( "XXTX" ) )
		|| ( 0 == s.compare( "XXXT" ) );
}

bool is_o( std::string const & s )
{
	return ( 0 == s.compare( "OOOO" ) )
		|| ( 0 == s.compare( "TOOO" ) )
		|| ( 0 == s.compare( "OTOO" ) )
		|| ( 0 == s.compare( "OOTO" ) )
		|| ( 0 == s.compare( "OOOT" ) );
}


result check_table( std::string const & s1,	std::string const & s2,
	std::string const & s3,	std::string const & s4 )
{
	if( is_x( s1 ) || is_x( s2 ) || is_x( s3 ) || is_x( s4 ) )
		return result_x;
	if( is_o( s1 ) || is_o( s2 ) || is_o( s3 ) || is_o( s4 ) )
		return result_o;

	std::string t1, t2, t3, t4;

	t1.push_back( s1[ 0 ] ); t1.push_back( s2[ 0 ] ); t1.push_back( s3[ 0 ] ); t1.push_back( s4[ 0 ] );
	t2.push_back( s1[ 1 ] ); t2.push_back( s2[ 1 ] ); t2.push_back( s3[ 1 ] ); t2.push_back( s4[ 1 ] );
	t3.push_back( s1[ 2 ] ); t3.push_back( s2[ 2 ] ); t3.push_back( s3[ 2 ] ); t3.push_back( s4[ 2 ] );
	t4.push_back( s1[ 3 ] ); t4.push_back( s2[ 3 ] ); t4.push_back( s3[ 3 ] ); t4.push_back( s4[ 3 ] );

	if( is_x( t1 ) || is_x( t2 ) || is_x( t3 ) || is_x( t4 ) )
		return result_x;
	if( is_o( t1 ) || is_o( t2 ) || is_o( t3 ) || is_o( t4 ) )
		return result_o;

	std::string d1, d2;

	d1.push_back( s1[ 0 ] ); d1.push_back( s2[ 1 ] ); d1.push_back( s3[ 2 ] ); d1.push_back( s4[ 3 ] );
	d2.push_back( s1[ 3 ] ); d2.push_back( s2[ 2 ] ); d2.push_back( s3[ 1 ] ); d2.push_back( s4[ 0 ] );

	if( is_x( d1 ) || is_x( d2 ) )
		return result_x;
	if( is_o( d1 ) || is_o( d2 ) )
		return result_o;

	bool is_dots( ( s1.find( '.' ) != std::string::npos ) || ( s2.find( '.' ) != std::string::npos )
		|| ( s3.find( '.' ) != std::string::npos ) || ( s4.find( '.' ) != std::string::npos ) );

	return is_dots ? result_not_completed : result_draw;
}



int main()
{
	std::ifstream ifs( "A-large.in", std::ifstream::in );

	std::string s;

	std::getline( ifs, s );

	size_t const count( atoi( s.c_str() ) );

	for( size_t i( 0 ); i != count; ++i )
	{
		std::string s1, s2, s3, s4;
		std::getline( ifs, s1 );
		std::getline( ifs, s2 );
		std::getline( ifs, s3 );
		std::getline( ifs, s4 );
		std::getline( ifs, s ); // empty line

		result const r( check_table( s1, s2, s3, s4 ) );

		std::cout << "Case #" << ( i + 1 ) << ": ";
		switch( r )
		{
			case result_x: std::cout << "X won"; break;
			case result_o: std::cout << "O won"; break;
			case result_draw: std::cout << "Draw"; break;
			case result_not_completed: std::cout << "Game has not completed"; break;
		}

		std::cout << std::endl;
	}

	return 0;
}
