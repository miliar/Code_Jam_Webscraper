#include	<iostream>
#include	<fstream>
#include	<sstream>
using	namespace	std;

#include	<boost/tokenizer.hpp>
using	namespace	boost;

#include	<math.h>

#include	<JpMooParaiso/Saturn.h>
using	namespace	JpMooParaiso::Saturn;
using	namespace	JpMooParaiso::Saturn::G;

long long	sDenos[ 14 ] =
{	1
,	10
,	100
,	1000
,	10000
,	100000
,	1000000
,	10000000
,	100000000
,	1000000000
,	10000000000
,	100000000000
,	1000000000000
,	10000000000000
};

bool
Fair( long long p )
{
	if ( p < 10 ) return true;
	if ( p < 100 ) return ( p / 10 ) == ( p % 10 );
	if ( p < 1000 ) return ( p / 100 ) == ( p % 10 );

	int	wDigit;
	     if ( p < 10000 ) wDigit = 4;
	else if ( p < 100000 ) wDigit = 5;
	else if ( p < 1000000 ) wDigit = 6;
	else if ( p < 10000000 ) wDigit = 7;
	else if ( p < 100000000 ) wDigit = 8;
	else if ( p < 1000000000 ) wDigit = 9;
	else if ( p < 10000000000 ) wDigit = 10;
	else if ( p < 100000000000 ) wDigit = 11;
	else if ( p < 1000000000000 ) wDigit = 12;
	else if ( p < 10000000000000 ) wDigit = 13;
	else if ( p < 100000000000000 ) wDigit = 14;
	else assert( false );
	long long wL = p;
	long long wH = p;
	for ( int i = 0; i < wDigit / 2; i++ )
	{
		if ( ( wL % 10 ) != wH / sDenos[ wDigit - 1 - i ] ) return false;
		wL /= 10;
		wH %= sDenos[ wDigit - 1 - i ];
	}
	return true;
}

Array<long long>	s;

void
Prepare()
{
	for ( long long i = 1; i < 10000000; i++ )
	{	if ( Fair( i ) )
		{	long long w = i * i;
			if ( Fair( w ) )
			{	s.Add( w );
				cout << w << "(" << i << ")" << endl;
			}
		}
	}
	s.ForAll( []( long long const& p ){ cout << p << ' '; } );
}

int
Find( long long pL, long long pH )
{
	int	wSize = (int)s.Size();

	int	wL = wSize;
	bool wF = false;
	while ( wL-- )
	{	if ( s[ wL ] < pL ) break;
		if ( s[ wL ] == pL )
		{	wF = true;
			break;
		}
	}

	int	wH = wSize;
	while ( wH-- )
	{	if ( s[ wH ] <= pH ) break;
	}
	
	int v = wH - wL;
	if ( wF ) v++;
cout << pL << " " << pH << " " << wL << " " << wH << " " << v << endl;
	return v;
}

int
main( int argc, char* argv[] )
{	assert( argc == 3 );
	cout << "I:" << argv[ 1 ] << endl;
	cout << "O:" << argv[ 2 ] << endl;

	ifstream wIFS( argv[ 1 ] );
	assert( wIFS.good() );
	ofstream wOFS( argv[ 2 ] );

	string	wLine;
	getline( wIFS, wLine );
	istringstream wISS( wLine );
	size_t	wT;
	wISS >> wT;

#if 1
	Prepare();
	for ( size_t i = 1; i <= wT; i++ )
	{
		cout << "#" << i << endl;

		long long	wL;
		long long	wH;
		{
			string	wLine;
			getline( wIFS, wLine );
			istringstream wISS( wLine );
			wISS >> wL;
			wISS >> wH;
		}
		int v = Find( wL, wH );
		wOFS << "Case #" << i << ": " << v << endl;
		cout << "Case #" << i << ": " << v << endl;
	}

#else
	struct
	Pair
	{	size_t	mK;
		string	mV;
	};
	__block	List<Pair>	v;

	dispatch_queue_t		wQ = ::dispatch_get_global_queue( DISPATCH_QUEUE_PRIORITY_DEFAULT, 0 );
	dispatch_group_t		wG = ::dispatch_group_create();
	dispatch_semaphore_t	wS = ::dispatch_semaphore_create( 1 );

	for ( size_t i = 1; i <= wT; i++ )
	{
		string	wS1;
		string	wS2;
		wIFS >> wS1;
		wIFS >> wS2;

		::dispatch_group_async
		(	wG
		,	wQ
		,	^{	Pair	w;
				w.mK = i;
				w.mV = Main( wS1, wS2 );
				::dispatch_semaphore_wait( wS, DISPATCH_TIME_FOREVER );
				v.Insert( w, [ & ]( Pair const& p ){ return w.mK > p.mK; } );
				::dispatch_semaphore_signal( wS );
			}
		);
	}

	::dispatch_group_wait( wG, DISPATCH_TIME_FOREVER );

	v.ForAll
	(	[ & ]( Pair const& p )
		{	wOFS << "Case #" << p.mK << ": " << p.mV << endl;
			cout << "Case #" << p.mK << ": " << p.mV << endl;
		}
	);
#endif
}
