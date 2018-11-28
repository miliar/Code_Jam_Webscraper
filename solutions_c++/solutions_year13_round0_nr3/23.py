//
// Qualification round 2013  problem C
//
// Usually built with g++ 4.4.5 on Linux
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <algorithm>
#include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

typedef mpz_class bigint;

unsigned int digits( bigint x )
{
     unsigned int n=0;
     while (x > 0)
     {
	  n++;
	  x /= 10;
     }
     return n;
}

unsigned int is_palindrome( bigint x )
{
     if (x==0) return true;
     unsigned int n = digits(x);

     bigint dd = 1;
     for (auto i=1u; i<n; i++) dd*=10;

     while (x>0)
     {
	  if (x/dd != x%10) return false;

	  x -= x/dd*dd;
	  x /= 10;
	  dd /= 100;
     }
     return true;
}

bigint reverse( bigint x, unsigned int n )
{
     bigint y=0;
     for (auto i=0u; i<n; i++)
     {
	  y *= 10;
	  y += x%10;
	  x /= 10;
     }
     return y;
}

bigint pow10( unsigned int n )
{
     if (n==0) return 1;
     if (n==1) return 10;
     bigint x = pow10(n/2);
     x *= x ;
     if (n%2 == 1) x*=10;
     //cout << "pow10(" << n << ") = " << x << endl;
     return x;
}

void process( vector<bigint> &vv, bigint x )
{
     if (!is_palindrome(x))
     {
	  cout << x << " is not a palindrome" << endl;
	  abort();
     }
     if (!is_palindrome(x*x))
     {
	  cout << x << " ";
	  cout << x*x << " is not a palindrome" << endl;
	  abort();
     }
     vv.push_back(x);
}
void process( vector<bigint> &vv, 
	      bigint s, 
	      unsigned int d,
	      bigint d10)
{
     if (0)
     {
	  cout << "Process "<< setw(20) << s ;
	  cout << " d = " << setw(2) << d << "  d10 = " << setw(20) << d10 << endl;
     }

     bigint r = reverse( s, d );
     process(vv, r*d10+s);
     process(vv, r*d10*10+s);
     process(vv, r*d10*10+d10+s);
}

int main( int argc, char ** argv )
{
     vector<bigint> vv;

     // 1, 2 and 3 squared are fair and square numbers
     vv.push_back(1);
     vv.push_back(2);
     vv.push_back(3);

     unsigned int max_digits = 27;

     bigint d10 = 1;
     for (auto d=1u; d<=max_digits;d++)
     {
	  cerr << "d = " << d << " of " << max_digits << endl;
	  d10 *= 10;

	  bigint r;
	  
	  process( vv, 1, d, d10 );

	  r = reverse(1, d );
	  vv.push_back( r*10*d10 + 2*d10 + 1 );
	  
	  r = reverse(2, d);
	  vv.push_back( r*d10 + 2 );
	  vv.push_back( r*10*d10 + 2);
	  vv.push_back( r*10*d10 + d10 + 2);
	  
	  for (auto j=1u; j<d; j++)
	  {
	       bigint s = pow10(j) + 1;
	       process( vv, s, d, d10 );

	       r = reverse(s, d);
	       process(vv, r*d10*10 + 2*d10 + s );
	  }
	  
	  for (auto j0=1u; j0<d; j0++)
	  {
	       for (auto j1=j0+1; j1<d; j1++)
	       {
		    bigint s = pow10(j0) + pow10(j1) + 1;
		    process( vv, s, d, d10 );
	       }
	  }
	  for (auto j0=1u; j0<d; j0++)
	  {
	       for (auto j1=j0+1; j1<d; j1++)
	       {
		    for (auto j2=j1+1; j2<d; j2++)
		    {
			 bigint s = pow10(j0) + pow10(j1) + pow10(j2) + 1;
			 process( vv, s, d, d10 );
		    }
	       }
	  }
     }
     
     sort(vv.begin(), vv.end());

     if (0)
     {
	  for (auto x : vv)
	  {
	       cout << setw(30) << x << " ";
	       cout << setw(60) << x*x << endl;
	       if (!is_palindrome(x*x))
	       {
		    cout << "ERROR" << endl;
		    exit(1);
	       }
	  }
     }
     cerr << "Table of fair and square has " << vv.size() << " members" << endl;

     for (auto i=0u; i<vv.size(); i++)
     {
	  vv.at(i) *= vv.at(i);
     }

     unsigned int t;

     cin >> t;

     for (auto i=1u; i<=t; i++) {

	  bigint a;
	  bigint b;

	  cin >> a;
	  cin >> b;

	  auto p1 = lower_bound(vv.begin(), vv.end(), a);
	  auto p2 = lower_bound(vv.begin(), vv.end(), b+1);
	  auto r = distance(p1,p2);

	  if (0)
	  {
	       unsigned int r=0;

	       for ( auto x : vv)
	       {
		    if (x>=a && x<=b) r++;
	       }
	  }

	  cout << "Case #" << i << ": ";
	  cout << r << endl;
     }

     return 0;
}

