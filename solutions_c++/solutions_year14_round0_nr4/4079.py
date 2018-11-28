#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

#define REP( i, N) for( int i = 0; (i < N); i ++ )
#define REP2( i , limit, N ) for( int i = limit; (i < N); i++ )

typedef vector<float> vi;
typedef vi::iterator vit;

int case_number;

void main2()
{
	int N;
	cin >> N;
	
	vi naomi;
	vi ken;
	REP( i , N )
	{
		float x;
		cin >> x;
		naomi.push_back( x );
	}

	for( auto j = 0 ; j < N ; j ++ )
	{
		float y;
		cin >> y;
		ken.push_back( y );
	}

	int war = 0;
	int deceived = 0;

	//====================================

	sort( naomi.begin(), naomi.end() );
	sort( ken.begin(), ken.end() );

	int n_end = (int)naomi.size() -1;
	int k_end = (int)ken.size() -1;
	int n_start = 0 ;
	int k_start = 0 ;
	for( ; n_end > -1 ; n_end-- )
	{
		if( naomi[ n_end ] > ken[ k_end ] )
		{
			war++;
			k_start ++; // naomi wins
		}
		else
		{
			k_end --; // ken wins
		}
	}

	//=====================================
	n_end = (int)naomi.size() -1;
	k_end = (int)ken.size() -1;
	n_start = 0 ;
	k_start = 0 ;

	REP( n_start , N )
	{
		if( naomi[ n_start ] < ken[ k_start ] )
		{
			k_end--; // kevin gives away min.
		}
		else
		{
			deceived ++;
			k_start ++;
		}
	}

	//=====================================

	cout << "Case #" << ++case_number << ": " << deceived << " " << war << endl;  

	
}

int main()
{
	int T;
	cin >> T;
	REP( i, T )
	{
		main2();
	}

}