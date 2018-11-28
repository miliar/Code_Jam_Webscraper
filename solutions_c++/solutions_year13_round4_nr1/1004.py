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
long long origin [1000] ;
long long dest [1000] ;
long long pop[1000] ;
int pairs ;
int n_stops ;
long long goal [1000] ;
long long elapsed [1000] ;
long long full [1000] ;
long long enter_at [1000] ;
long long exit_at [1000] ;

#define STOP 100
// dp [
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
cin >> n_stops ;
cin >> pairs ;
for ( int i = 0 ; i < pairs ; i ++ )
   cin >> origin[i] >> dest[i] >> pop[i] ;
for ( int i = 0 ; i < pairs ; i ++ )
   {
   --origin[i] ;
   --dest[i] ;
   }

   
long long base_score = 0 ;
for ( int i = 0 ; i < pairs ; i ++ )
   {
   long long d = dest[i]-origin[i] ;
   base_score += (n_stops * d - d*(d-1)/2) * pop[i] ;
   //cout << "base = " << base_score << endl ;
   }

// for ( long long d = 0 ; d < 6 ; d ++ )
//    cout << d << ": " << n_stops * d << " " << - d*(d-1)/2 << endl ;


for ( int i = 0 ; i < n_stops+1 ; ++ i )
   enter_at[i] = exit_at[i] = full[i] = goal[i] = 0 ;

long long on_train = 0 ;
for ( int t = 0 ; t < n_stops ; ++ t )
   {
   // travel to station
   // at station t
   // people enter
   for ( int j = 0 ; j < pairs ; j ++ )
      if ( origin[j] == t )
         {
         goal[dest[j]] += pop[j] ;
         elapsed[0] += pop[j] ;
         full[t] += pop[j] ;
         enter_at[t] += pop[j] ;
         on_train += pop[j] ;
         }
   // people exit
   for ( int i = n_stops - 1 ; i > 0 ; i -- )
      elapsed [i] = elapsed[i-1] ;
   elapsed[0] = 0 ;
   
   for ( int j = 0 ; j < pairs ; j ++ )
      if ( dest[j] == t )
         {
         goal[t] -= pop[j] ;
         exit_at[t] += pop[j] ;
         on_train -= pop[j] ;
         }

   full[t] = on_train ;
   // travel to next station
   }

// for ( int i = 0 ; i < n_stops ; i ++ )
//    cout << full[i] << " "  ;
// cout << enld ;

long long cost = 0 ;
for ( int len = n_stops-1 ; len > 0 ; --len )
   {
   for ( int start = 0 ; start < n_stops - len ; start ++ )
      {
      long long max_riders = 1000000000000000LL ;
      for ( int i = start ; i <= start+len-1 ; i ++ )
         {
         max_riders = min ( max_riders, full[i] ) ;
         if ( max_riders <= 0 ) break ;
         }
      //      cout << "len = " << len << " start = " << start << " rider = " << max_riders << endl ;
      
      if ( max_riders <= 0 ) continue ;

      // if ( max_riders > 0 )
      //    cout << max_riders << " from " << start << " len = " << len << " score = "
      //         << max_riders * ( len * n_stops - len*(len-1)/2 ) << endl ;
      
      for ( int i = start ; i <= start+len-1 ; i ++ )
         full[i] -= max_riders ;
      cost += max_riders * ( len * n_stops - len*(len-1)/2 ) ;
      }
   }


cout << "Case #" << case_number << ": " ;
cout << base_score - cost ;
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
