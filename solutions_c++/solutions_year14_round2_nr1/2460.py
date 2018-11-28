#include <iostream>
#include <vector>	//vector
#include <string.h>
#include <utility>	//pair
using namespace std;

typedef pair<char, short> mypair;

inline int min( int a, int b ){ return a > b ? b : a; }
inline int max( int a, int b ){ return a > b ? a : b; }

int main(){
	int t, nT, N;
	char buff[ 105 ]={ 0, }, prev[ 105 ]={ 0, };

	cin >> nT;
	for( t=1; t <= nT; ++t )
	{
		cin >> N;
		vector < mypair > *line = new vector< mypair > [ N ];
		
		char result = 0;
		int minSize = 0;
		for( int n=0; n < N; ++n ){
			cin >> buff;

			int countIden = 1, len = strlen( buff );
			for( int b=0; b < len; ++b )
			{
				if( buff[ b ] != buff[ b+1 ] || b == len - 1 ){
					line[ n ].push_back( mypair( buff[ b ], countIden ) );
					countIden = 1;
				}
				else
					++countIden;
			}


			if( n == 0 )
				minSize = line[ n ].size();
			else if( minSize != line[ n ].size() ){
				result = -1;
				//cout<<"\nbreak!\n";
				break;
			}
		}

		int calcD = 0;

		if( result != -1 )
		{
			for( int idx = 0; idx < minSize; ++idx )
			{
				int minD = line[ 0 ].at( idx ).second;
				int maxD = minD;

				for( int n=1; n < N; ++n ){
					if( line[ n-1 ].at( idx ).first != line[ n ].at( idx ).first ){
						result = -1;
						//cout<<"\nbreak!\n";
						break;
					}

					int temp = line[ n ].at( idx ).second;
					minD = min( minD, temp );
					maxD = max( maxD, temp );
				}

				calcD += ( maxD - minD );
			}
		}

		cout<<"Case #"<< t <<": ";
		if( result == -1 ) cout<< "Fegla Won\n";
		else cout<< calcD <<endl;

		delete [] line;
		line = NULL;
	}
}