#include <cstdio>
#include <deque>
#include <algorithm>

void Load( int & N, std::deque<double> & naomi, std::deque<double> & ken )
{
	double dummy;
	scanf( "%d", & N );

	for( int i = 0; i < N; i++ )
	{
		scanf( "%lf", & dummy);
		naomi.push_back( dummy );
	}
	for( int i = 0; i < N; i++ )
	{
		scanf( "%lf", & dummy);
		ken.push_back( dummy );
	}

	/*
	for( double i : naomi )
		printf("%.5lf ", i );
	printf("\n");

	for( double i : ken )
		printf("%.5lf ", i );
	printf("\n");
	*/

	std::sort( naomi.begin(), naomi.end() );
	std::sort( ken.begin(), ken.end() );
}

int War( std::deque<double> naomi, std::deque<double> ken )
{
	int naomiPts = 0;

	for( const double & nChoice : naomi )
	{
		auto kChoiceIt = std::find_if( ken.begin( ), ken.end( ), [ nChoice ]( double a ) -> bool{
			return a > nChoice;
		} );

		if( kChoiceIt == ken.end( ) )
		{
			ken.erase( ken.begin( ) );
			naomiPts += 1;
		}
		else
		{
			ken.erase( kChoiceIt );
		}
	}

	return naomiPts;
}

int dWar( std::deque<double> & naomi, std::deque<double> & ken )
{
	int naomiPts = 0;
	int kenPts = 0; //debug

	// destroy all ken's brickes that are heavier than naomi's
	// naomi uses her lightest
	while( ! ken.empty( ) && * ken.rbegin( ) > * naomi.rbegin( ) )
	{
		naomi.erase( naomi.begin( ) );
		ken.erase( std::prev( ken.end( ) ) );
		kenPts += 1;
	}

	// Naomi tells Ken that she has heavier than his heaviest.
	// Ken uses his lightest, Naomi uses first heavier than Ken's
	while( true )
	{
		auto nChoiceIt = std::find_if( naomi.begin( ), naomi.end( ), [ ken ]( double a ) -> bool{
			return a > * ken.begin( );
		} );

		if( nChoiceIt == naomi.end( ) )
			break;

		naomi.erase( nChoiceIt );
		ken.erase( ken.begin( ) );
		naomiPts += 1;
	}

	// printf("%lu - ", ken.size());

	naomiPts += War( naomi, ken );

	// printf("Debug: KEN: %d, NAO: %d\n", kenPts, naomiPts );
	return naomiPts;
}

void Solve( int caseId )
{
	int N;
	std::deque<double> naomi, ken;

	Load( N, naomi, ken );

	int war = War( naomi, ken );
	int dwar = dWar( naomi, ken ); // destroys sets!
	printf("Case #%d: %d %d\n", caseId, dwar, war );
}

int main()
{
	int cases;
	scanf( "%d\n", & cases );
	for( int i = 1; i <= cases; i++ )
		Solve( i );
	return 0;
}