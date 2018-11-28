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
const bool use_multi = false;
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

   int n;
   vector<int> v;

	void read()
	{
      cin >> n;
      v.resize( n );
      ::read( v );
	}

	result_type solve()
	{
      int ans2 = -1;
/*      vector<int> u = v;
      sort( u.begin(), u.end() );
      do
      {
         int i;
         for( i = 1; i < n; ++i )
         {
            if( u[ i ] < u[ i - 1 ] )
               break;
         }
         for( ; i < n; ++i )
         {
            if( u[ i ] > u[ i - 1 ] )
               break;
         }
         if( i == n )
         {
            int tmp = 0;
            for( i = 0; i < n; ++i )
            for( int j = 0; j < n; ++j )
            if( v[ i ] == u[ j ] )
            {
               tmp += abs( i - j );
               break;
            }
            
            tmp /= 2;
            if( ans2 == -1 )
               ans2 = tmp;
            else
               ans2 = min( ans2, tmp );
         }
         

      } while( next_permutation( u.begin(), u.end() ) );
      */

      vector<int> bleft( n ), bright( n );
      int i, j, ans = 0;
      for( i = 0; i < n; ++i )
      {
         bleft[ i ] = bright[ i ] = 0;
         for( j = 0; j < i; ++j )
         {
            if( v[ j ] > v[ i ] )
               ++bleft[ i ];
         }
         for( j = i + 1; j < n; ++j )
         {
            if( v[ j ] > v[ i ] )
               ++bright[ i ];
         }
         ans += min( bleft[ i ], bright[ i ] );
      }
      return ans;
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
   open_files( "b-large.in", "b-large.out" );

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