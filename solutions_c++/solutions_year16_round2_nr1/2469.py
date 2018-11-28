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
void do_case ( int case_number )
// ****************************************************************************
{
string x ;
cin >> x ;

 int lct [255] ;
 int dct [10] ;
 
 for ( int i = 0 ; i < 10 ; ++i )
   dct[i] = 0 ;

 for ( int i = 'A' ; i <= 'Z' ; ++i )
   lct[i] = 0 ;

 for ( int i = 0 ; i < x.size() ; ++i )
   ++lct[x[i]] ;

 dct[0] += lct['Z'] ;
 lct['Z'] -= dct[0] ;
 lct['E'] -= dct[0] ;
 lct['R'] -= dct[0] ;
 lct['O'] -= dct[0] ;

 dct[2] += lct['W'] ;
 lct['T'] -= dct[2] ;
 lct['W'] -= dct[2] ;
 lct['O'] -= dct[2] ;

 // one three four five six seven eight nine

 dct[6] += lct['X'] ;
 lct['S'] -= dct[6] ;
 lct['I'] -= dct[6] ;
 lct['x'] -= dct[6] ;

 // one three four five seven eight nine

 dct[4] += lct['U'] ;
 lct['F'] -= dct[4] ;
 lct['O'] -= dct[4] ;
 lct['U'] -= dct[4] ;
 lct['R'] -= dct[4] ;

 // one three five seven eight nine

 dct[5] += lct['F'] ;
 lct['F'] -= dct[5] ;
 lct['I'] -= dct[5] ;
 lct['V'] -= dct[5] ;
 lct['E'] -= dct[5] ;

 // one three seven eight nine

 dct[1] += lct['O'] ;
 lct['O'] -= dct[1] ;
 lct['N'] -= dct[1] ;
 lct['E'] -= dct[1] ;

 // three seven eight nine

 dct[3] += lct['R'] ;
 lct['T'] -= dct[3] ;
 lct['H'] -= dct[3] ;
 lct['R'] -= dct[3] ;
 lct['E'] -= dct[3] ;
 lct['E'] -= dct[3] ;

 // seven eight nine

 dct[7] += lct['V'] ;
 lct['S'] -= dct[7] ;
 lct['E'] -= dct[7] ;
 lct['V'] -= dct[7] ;
 lct['E'] -= dct[7] ;
 lct['N'] -= dct[7] ;

 // eight nine

 dct[8] += lct['G'] ;
 lct['E'] -= dct[8] ;
 lct['I'] -= dct[8] ;
 lct['G'] -= dct[8] ;
 lct['H'] -= dct[8] ;
 lct['T'] -= dct[8] ;

 dct[9] = lct['I'] ;

string answer = "" ;
 for ( int d = 0 ; d < 10 ; ++d )
   for ( int i = 0 ; i < dct[d] ; ++i )
     answer += (char)('0'+d) ;

cout << "Case #" << case_number << ": " ;
cout <<  answer ;
cout << endl ;
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ; getchar() ;
for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************
