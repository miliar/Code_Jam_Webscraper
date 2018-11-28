#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <thread>
#include <mutex>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

namespace
{
	const ll mod = 1000002013;

	template<class T>
	void read( T& container )
	{
		for( typename T::value_type& x : container )
			cin >> x;
	}

	template<class T>
	void print( T& container, const string& separator = " " )
	{
		for( typename T::value_type& x : container )
			cout << x << separator;
	}

	void openFiles( const char* in, const char* out )
	{
		freopen( in, "r", stdin );
		freopen( out, "w", stdout );
	}
 
	// test result type definition
	typedef ll ResultType;

	struct Train
	{
		ll pas;
		int a;
		int b;
	};

	bool operator < ( const Train& lhs, const Train& rhs )
	{
		if( lhs.a == rhs.a ) return lhs.b < rhs.b;
		return lhs.a < rhs.a;
	}

	struct Solver
	{
		// solution code here
		Solver() {}

		vector<pair<ll, ll>> v;
		ll n, m;
		
		void read()
		{
			v.clear();
			cin >> n >> m;
			int p;
			int i, j;
			ll a, b;
			for( i = 0; i < m; ++i )
			{
				cin >> a >> b >> p;
				while( p-- )
					v.push_back( make_pair( a, b ));
			}
			sort( v.begin(), v.end());
			m = v.size();
		}

		ResultType solve()
		{
			ll normalRes = 0;
			int i, j;
			for( i = 0; i < m; ++i )
			{
				ll k = v[ i ].second - v[ i ].first;
				normalRes += n * ( n + 1 ) / 2 - k * ( k + 1 ) / 2;
				normalRes %= mod;
			}
			for( i = 0; i < m; ++i )
				for( j = i + 1; j < m; ++j )
					if( v[ j ].first > v[ i ].second )
						break;
					else if( v[ j ].second > v[ i ].second )
						swap( v[ i ].second, v[ j ].second );
			ll thisRes = 0;
			for( i = 0; i < m; ++i )
			{
				ll k = v[ i ].second - v[ i ].first;
				thisRes += n * ( n + 1 ) / 2 - k * ( k + 1 ) / 2;
				thisRes %= mod;
			}
			normalRes -= thisRes;
			if( normalRes < 0 )
				normalRes += mod;
			return normalRes;
		}
	};


	mutex resultLocker;
	vector<ResultType> result;
	vector<thread> threads;
	vector<Solver> solvers;

	void run( int testNumber )
	{
		ResultType res = solvers[ testNumber ].solve();
		resultLocker.lock();
		result[ testNumber ] = res;
		resultLocker.unlock();
	}

	void printResult( int testNumber )
	{
		cout << "Case #" << testNumber + 1 << ": "; // default
		cout << result[ testNumber ] << endl;
	}

	const bool useMulti = 0;

	void process() 
	{ 
	//	freopen( "A-small.in", "r", stdin );
		openFiles( "A-small.in", "A-small.out" );
		// preparations
		int testCount;
		cin >> testCount;
		threads.resize( testCount );
		result.resize( testCount );
		solvers.resize( testCount );

		// input
		for( int i = 0; i < testCount; ++i )
		{
			solvers[ i ].read();
		//	run( i );
		//	printResult( i );
		}
	//	return;

		// detach threads if necessary
		if( useMulti )
		{
			for( int i = 0; i < testCount; ++i )
				threads[ i ] = thread( run, i );
			for( int i = 0; i < testCount; ++i )
				threads[ i ].join();
		}
		else
		{
			for( int i = 0; i < testCount; ++i )
				run( i );
		}
		for( int i = 0; i < testCount; ++i )
			printResult( i );
	}
}

int main() { process(); return 0; }