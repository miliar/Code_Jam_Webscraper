
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int tests;


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{

		int N, M;
		cin >> N >> M;

		vector< vector<int> > a( N, vector<int>( M, 0 ) );
		for( int i=0; i<N; ++i ) for( int j=0; j<M; ++j ) cin >> a[i][j];

		int ma = 0;
		for( int i=0; i<N; ++i ) for( int j=0; j<M; ++j )
			if ( a[i][j] > ma ) ma = a[i][j];

		bool res = true;
		for( int i=0; i<N; ++i ) for( int j=0; j<M; ++j )
		{
			if ( a[i][j] < ma )
			{
				// check row or col
				const auto kAV = a[i][j];
				bool okv = true, okh = true;
				for( int x=0; x<N; ++x ) if ( a[x][j] > kAV ) okv = false;
				for( int x=0; x<M; ++x ) if ( a[i][x] > kAV ) okh = false;
				if ( !okv && !okh ) res = false;
			}
		}

		cout << "Case #" << (curTest+1) << ": ";
		cout << (res?"YES":"NO");
		cout << endl;
	}

	return 0;
}

