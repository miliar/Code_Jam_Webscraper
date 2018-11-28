// ****************************************************************************
// Code developed starting from Rustyoldman's Google Code jam template
// ****************************************************************************
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cstdlib>
#define enld endl
using namespace std ;
// ****************************************************************************
int getchar ( )
// ****************************************************************************
{
if ( cin.eof() )
   return -1 ;
int ch = cin.get() ;
if ( cin.fail() )
   return -1 ;
return ch ;
}
// ****************************************************************************
string tokenstartchars 
= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
string tokenchars 
= ".0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
// ****************************************************************************
string gettoken ( )
// ****************************************************************************
{
int ch ;

ch = cin.get() ;

while ( ! cin.eof () && (ch == ' ' || ch == '\n') )
   ch = getchar ( ) ;

if ( ch == -1 )
   return "ERROR" ;

string ans = "" ;
if ( tokenstartchars.find( (char) ch ) != string::npos ) 
   {
   while ( tokenchars.find ( (char) ch ) != string::npos)
      {
      ans.push_back((char) ch) ;
      ch = getchar ( ) ;
      }
   cin.putback((char)ch) ;
   return ans ;
   }

ans = "" ;
ans.push_back ( (char) ch ) ;
return ans ;
}
// ****************************************************************************
double getdouble ( ) 
// ****************************************************************************
{
double a ;
cin >> a ;
return a ;
}
// ****************************************************************************
int getint ( ) 
// ****************************************************************************
{
while ( cin.peek ( ) == ' ' || cin.peek ( ) == '\n' )
   getchar ( ) ;
int sign = 1 ;
if ( cin.peek ( ) == '-' )
   {
   sign = -1 ;
   getchar ( ) ;
   }
string toke = gettoken ( ) ;
if ( sign == -1 && toke == "2147483648" )
   return -2147483648 ;

return sign * atoi ( toke.c_str() ) ;
}
// ****************************************************************************
vector<string> values ;
int magic = 41551 ;
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
string a , b ;
cin >> a >> b ;

int c = 0 ;
for ( int i = 0 ; i < values.size() ; ++i )
   if ( ( a.size() < values[i].size() || a.size() == values[i].size () && a <= values[i] ) &&
        ( b.size() > values[i].size() || b.size() == values[i].size () && b >= values[i] ) ) 
      c++ ;

cout << "Case #" << case_number << ": " << c ;
cout << endl ;
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ; getchar() ;

ifstream pref ( "precomputed.fair_and_square" ) ;

string val ;
values.resize(magic) ;
for ( int i = 0 ; i < magic ; ++i )
   {
   pref >> values[i] ;
   }

for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************



// The precomputation program that was used follows below.

// #include <string>
// #include <vector>
// #include <iostream>

// using namespace std ;

// int ans = 0 ;

// void print ( vector<int> & a )
// {
// for ( int i = a.size ( )-1 ; i >= 0 ; --i )
//    cout << a[i] ;
// }

// void norm ( vector<int> & a )
// {
// int n = a.size() ;
// for ( int i = 0 ; i < n ; ++i )
//    if ( a[i] > 9 )
//       {
//       if ( i == n - 1 )
//          {
//          a.resize ( n+1 ) ;
//          a[i] = 0 ;
//          }
//       a[i+1] += a[i]/10 ;
//       a[i] %= 10 ;
//       }
// }


// void square( vector<int> & a , vector<int> & c )
// {
// int n = a.size() ;
// int s = n+n-1 ;
// c.resize ( s ) ;
// for ( int i = 0 ; i < s ; ++i )
//    c[i] = 0 ;
// for ( int i = 0 ; i < n ; ++i )
//    for ( int j = 0 ; j < n ; ++j )
//       c[i+j] += a[i]*a[j] ;
// // if ( a.size() == 6 )
// //    {
// //    print ( a ) ;
// //    cout << endl ;
// //    for ( int i = 0 ; i < c.size() ; ++i ) 
// //       cout << c[i] << " " ;
// //    cout << endl ;
// //    }

// norm ( c ) ;
// // if ( a.size() == 6 )
// //    {
// //    for ( int i = 0 ; i < c.size() ; ++i ) 
// //       cout << c[i] << " " ;
// //    cout << endl ;
// //    }

// }


// int pal ( vector<int> & a )
// {
// int n = a.size() ;
// for ( int i = 0 ; i < n ; ++i )
//    if ( a[i] != a[n-i-1] )
//       return 0 ;
// return 1 ;
// }




// void test_it ( vector<int> & small )
// {
// vector<int> big ;

// square ( small , big ) ;
// if ( pal ( big ) ) 
//    {
//    // print ( big ) ;
//    // cout << " " ;
//    ++ ans ;
//    // cout << ans << " " << small.size() << " " ;

//    // print ( small ) ;
//    // cout << endl ;
//    // cout << "\"" ;
//    print ( big ) ;
//    // cout << "\"," ;
//    cout << endl ;
//    }
// }


// int generate  ( vector<int> & pf , int n , int pos )
// {

// if ( pos == n )
//    {
//    vector<int> small_pal ( n+n-1) ;
//    for ( int i = 0 ; i < n ; ++i )
//       small_pal[n+n-i-2] = small_pal [i] = pf[i] ;
//    test_it ( small_pal ) ;
   

//    small_pal.resize ( n+n ) ;
//    for ( int i = 0 ; i < n ; ++i )
//       small_pal[n+n-i-1] = small_pal [i] = pf[i] ;
//    test_it ( small_pal ) ;
   
//    return 0 ;
//    }


// if ( pos > 0 )
//    {
//    pf[pos] = 0 ;
//    generate ( pf , n , pos+1 ) ;
//    }
// else 
//    {
//    pf[pos] = 3 ;
//    generate ( pf , n , pos+1 ) ;
//    }
// pf[pos] = 1 ;
// generate ( pf , n , pos+1 ) ;
// if ( pos == 0 || pos == n-1 ) 
//    {
//    pf[pos] = 2 ;
//    generate ( pf , n , pos+1 ) ;
//    }
// }


// int main ( int argc , char ** argv )
// {
// for ( int length = 1 ; length <= 26 ; ++length )
//    {
//    vector<int> postfix ( length ) ;
//    generate ( postfix , length , 0 ) ;
//    //   cout << endl ;
   

//    }


// }
