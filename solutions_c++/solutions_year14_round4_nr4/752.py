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
typedef pair<int, int> result_type;
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

int tn;

struct solver
{
	// solution code here
	solver() {}

   int m, n;
   vector<string> s;
   vector<int> serv;

	void read()
	{
      cin >> m >> n;
      s.resize( m );
      serv.resize( m );
      ::read( s );
	}

   int count( int mask )
   {
      unordered_set<string> st;
      for( int i = 0; i < m; ++i )
      if( mask & ( 1 << i ) )
      {
         for( int j = 0; j <= s[ i ].size(); ++j )
         {
  //          cout << s[ i ].substr( 0, j ) << endl;
            st.insert( s[ i ].substr( 0, j ) );
         }
      }
    //  cout << endl;
      return st.size();
   }

   pair<int, int> res;

   void doit( int i )
   {
      if( i == m )
      {
         int tmp = 0;
         for( int srv = 0; srv < n; ++srv )
         {
            int mask = 0;
            for( int j = 0; j < m; ++j )
            if( serv[ j ] == srv )
               mask ^= ( 1 << j );

            tmp += count( mask );
           
         } if( tmp > res.first )
         {
            res = make_pair( tmp, 1 );
         }
         else if( tmp == res.first )
            ++res.second;
      }
      else
      {
         for( int j = 0; j < n; ++j )
         {
            serv[ i ] = j;
            doit( i + 1 );
         }
      }
   }

	result_type solve()
	{
      res = make_pair( -1, -1 );
      doit( 0 );
  //    cerr << "done " << tn << endl;
      return res;
	}
};


mutex result_locker;
vector<result_type> results;
vector<thread> threads;
vector<solver> solvers;

void run( int test_num )
{
 //  tn = test_num;
	result_type res = solvers[ test_num ].solve();
	result_locker.lock();
	results[ test_num ] = res;
	result_locker.unlock();
}

void print_result( int test_num )
{
	cout << "Case #" << test_num + 1 << ": "; // default
	// print code here
   cout << results[ test_num ].first << ' ' << results[ test_num ].second << endl;
}

void process() 
{ 
   open_files( "d-small-1.in", "d-small-1.out" );

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