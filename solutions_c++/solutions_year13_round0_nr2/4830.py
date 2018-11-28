// lawnmorwer.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef std::vector< size_t > Row;
typedef std::vector< size_t >::iterator RowIt;
typedef std::vector< Row > Lawn;
typedef std::vector< Row >::iterator LawnIt;

//true is failed
bool check_row( Lawn& lawn, size_t n, size_t m )
{
	size_t h= lawn[ n ][ m ];
	for( RowIt it= lawn[ n ].begin( ); it < lawn[ n ].end( ); ++it )
		if( h < *it )
			return true;
	return false;
}

bool check_col( Lawn& lawn, size_t n, size_t m )
{
	size_t h= lawn[ n ][ m ];
	for( LawnIt it= lawn.begin( ); it < lawn.end( ); ++it )
		if( h < it->at( m ) )
			return true;
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::fstream is( "in.txt", std::ios::in );
	size_t count;
	is >> count;
	std::fstream os( "out.txt", std::ios::ate | std::ios::out );

	for( size_t i= 0; i < count; ++i )
	{
		size_t n;//lines
		size_t m;
		is >> n >> m;
		Lawn lawn( n );
		for( LawnIt it= lawn.begin( ); it != lawn.end( ); ++ it )
			it->resize( m );

		for( size_t nc= 0; nc < n; ++nc )
			for( size_t mc= 0; mc < m; ++mc )
			{
				size_t s;
				is >> s;
				lawn[ nc ][ mc ]= s;
			}

		//now....
		bool bFailed= false;
		for( size_t nc= 0; nc < n; ++nc )
			for( size_t mc= 0; mc < m; ++mc )
			{
				if( check_row( lawn, nc, mc )
					&& check_col( lawn, nc, mc ) )
				{
					bFailed= true;
					break;
				}
			}

		os << "Case #" << i + 1 << ": " << ( bFailed ? "NO" : "YES" ) << std::endl;
	}

	return 0;
}

