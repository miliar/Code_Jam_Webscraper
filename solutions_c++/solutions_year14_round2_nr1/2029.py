/* Gansito144 */
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<memory.h>
#include<utility>
#include<vector>
#include<set>

#define F first
#define S second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long int i64;

typedef pair < char , int  > tip;

int main()
{	
	int T , N , cnt, idx, ANS, wL;
	string word;
	bool isAnswer;
	
	cin >> T;
	for( int ca  = 1 ; ca <= T; ca++ )
	{
		cin >> N;
		vector < tip > All[ N ];
		isAnswer = true;
		wL = -1;
		
		// Split strings in way C1L1 , C2L2 ... CNLN
		for( int i = 0; i < N ; i++ )
		{
			cin >> word;
			char ant = 0; idx = 0;
			while( isAnswer && idx < word.size() )
			{	
				if( word[ idx ] != ant )
				{
					All[ i ].pb( mp( word[ idx ] , 0 ) );
				}
				All[ i ][ All[i].size() - 1 ].S++;
				ant = word[ idx ];
				idx++;
			}
			if( wL != -1 && All[ i ].size() != wL )
			{
				isAnswer = false;
			}
			wL = All[ i ].size();
		}
		
		if( !isAnswer ) // If the words don't have the equal size
		{
			
			cout << "Case #" << ca << ": " << "Fegla Won" << endl;
		}
		else
		{
			vector < int > Cnt( wL , 0 );
			for( int i = 1; i < N && isAnswer ; i++ )
			{
				for( int j = 0; j < wL ; j++ )
				{
					if( All[i-1][j].F != All[i][j].F )
					{
						isAnswer = false;
						break;
					}
					if( i == 1 ) Cnt[ j ] += All[0][j].S;
					Cnt[ j ] += All[ i ][ j ].S;
					
				}
			}
			if( !isAnswer ) // If the words don't have the same Letters 
			{
				cout << "Case #" << ca << ": " << "Fegla Won" << endl;
			}
			else
			{	// Now we calculate the average and answer
				ANS = 0; // The moves
				for( int j = 0; j < wL ; j++ )
				{
					Cnt[ j ] /= N; // Average
					for( int i = 0; i < N ; i++ )
					{
						ANS += abs( All[ i ][ j ].S - Cnt[ j ] );
					}
				}
				cout << "Case #" << ca << ": " << ANS << endl;
			}
		}
	}
	return 0;
}
