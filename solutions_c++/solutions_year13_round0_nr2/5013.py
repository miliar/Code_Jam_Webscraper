#include	<iostream>
#include	<fstream>
#include	<sstream>
using	namespace	std;

#include	<boost/tokenizer.hpp>
using	namespace	boost;

#include	<math.h>

//#include	<JpMooParaiso/Saturn.h>
//using	namespace	JpMooParaiso::Saturn;
//using	namespace	JpMooParaiso::Saturn::G;

struct
Lawn
{
	int		mN;
	int		mM;
	char*	m;
	Lawn( int pN, int pM, char* p )
	:	mN( pN )
	,	mM( pM )
	,	m( p )
	{
	}
	char&
	E( int pN, int pM )
	{	return m[ pN * mM + pM ];
	}

	bool
	Check( int pN, int pM )
	{	int w = E( pN, pM );
		for ( int n = 0; n < pN; n++ ) if ( E( n, pM ) > w ) return false;
		for ( int n = pN + 1; n < mN; n++ ) if ( E( n, pM ) > w ) return false;
		for ( int m = 0; m < pM; m++ ) if ( E( pN, m ) > w ) return false;
		for ( int m = pM + 1; m < mM; m++ ) if ( E( pN, m ) > w ) return false;
		return true;
	}

	bool
	HBlock( int p, int pN, int pM )
	{	for ( int m = 0; m < pM; m++ ) if ( p < E( pN, m ) ) return true;
		for ( int m = pM + 1; m < mM; m++ ) if ( p < E( pN, m ) ) return true;
		return false;
	}
	bool
	VBlock( int p, int pN, int pM )
	{	for ( int n = 0; n < pN; n++ ) if ( p < E( n, pM ) ) return true;
		for ( int n = pN + 1; n < mN; n++ ) if ( p < E( n, pM ) ) return true;
		return false;
	}
	bool
	Check()
	{
		for ( int n = 0; n < mN; n++ )
		{	for ( int m = 0; m < mM; m++ )
			{	int	w = E( n, m );
				if ( HBlock( w, n, m ) && VBlock( w, n, m ) ) return false;
			}
		}
		return true;
	}
	void
	Dump()
	{	for ( int n = 0; n < mN; n++ )
		{	for ( int m = 0; m < mM; m++ ) cout << E( n, m ) << ' ';
			cout << endl;
		}
	}
};

int
main( int argc, char* argv[] )
{
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
	for ( size_t i = 1; i <= wT; i++ )
	{
		cout << "#" << i << endl;

		int	wN;
		int	wM;
		{
			string	wLine;
			getline( wIFS, wLine );
			istringstream wISS( wLine );
			wISS >> wN;
			wISS >> wM;
		}
		char	w[ wN * wM ];
		for ( int n = 0; n < wN; n++ )
		{
			string wLine;
			getline( wIFS, wLine );
			istringstream wISS( wLine );
			for ( int m = 0; m < wM; m++ )
			{	wISS >> w[ n * wM + m ];
			}
		}
		string v = Lawn( wN, wM, w ).Check() ? "YES" : "NO";
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

	for ( size_t i = 0; i < wT; i++ )
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
		{	wOFS << "Case #" << ( p.mK + 1 ) << ": " << p.mV << endl;
			cout << "Case #" << ( p.mK + 1 ) << ": " << p.mV << endl;
		}
	);
#endif
}
