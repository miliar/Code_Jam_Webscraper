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

// globals
typedef int result_type;
const bool use_multi = true;
//


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

void open_files( const char* in, const char* out )
{
   if( in )
	   freopen( in, "r", stdin );
   if( out )
	   freopen( out, "w", stdout );
}

struct solver
{
	// solution code here
	solver() {}

   int n, m;
   vector<int> s;

	void read()
	{
      cin >> n >> m;
      s.resize( n );
      for( auto& x : s )
         cin >> x;
	}

	result_type solve()
	{
      sort( s.begin(), s.end() );
      int res = 0;
      vector<char> used( n, 0 );

      int i, j;
      for( i = n - 1; i >= 0; --i )
      {
         if( !used[ i ] )
         {
            ++res;
            used[ i ] = 1;
            for( j = i - 1; j >= 0; --j )
            {
               if( !used[ j ] && s[ i ] + s[ j ] <= m )
               {
                  used[ j ] = 1;
                  break;
               }
            }
         }
      }

      return res;
	}
};


mutex result_locker;
vector<result_type> results;
vector<thread> threads;
vector<solver> solvers;

void run( int test_num )
{
	result_type res = solvers[ test_num ].solve();
	result_locker.lock();
	results[ test_num ] = res;
	result_locker.unlock();
}

void print_result( int test_num )
{
	cout << "Case #" << test_num + 1 << ": "; // default
	// print code here
   cout << results[ test_num ] << endl;
}

void process() 
{ 
   open_files( "a-large.in", "a-large.out" );

	// preparations
	int test_count;
	cin >> test_count;
	threads.resize( test_count );
	results.resize( test_count );
	solvers.resize( test_count );

	// input
	for( int i = 0; i < test_count; ++i )
		solvers[ i ].read();


	// detach threads if necessary
	if( use_multi )
	{
		for( int i = 0; i < test_count; ++i )
			threads[ i ] = thread( run, i );
		for( int i = 0; i < test_count; ++i )
			threads[ i ].join();
	}
	else
	{
		for( int i = 0; i < test_count; ++i )
			run( i );
	}
	for( int i = 0; i < test_count; ++i )
		print_result( i );
}

int main() { process(); return 0; }