#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<fstream>
#include<cstdlib>

#define lld long long 
#define llu unsigned long long //No need to write int ahead of long long 
 
using namespace std ;

int main()
{
  int T, Smax, i, min, count, t ; 
  char S[1002] ;
  ifstream infile ;       // input file object
  ofstream outfile;       // output file object
  infile.open ("A-small-attempt1.in") ; 
  infile >> T ;
  /*for( int i = 0 ; i < n ; i++ )
    outfile << A[i] << "\n" ;*/
  outfile.open( "out_ovation1.txt") ;                                                   //chang name if input txt file changes
  for( t = 1 ; t <= T ; t++ )
    {
      infile >> Smax ;
      infile >> S ;
      //char S[Smax+1] ;
      min = 0 ; 
      count = S[0] - 48 ;
      if( Smax == 0 && S[Smax] == '0' )
	min = 1 ;
      else
	{
	  for( i = 1 ; i <= Smax ; i++ )
	    {
	      if( i > count && S[i] != '0' )
		{
		  min += i - count ;
		  count += S[i] - 48 + min ;
		}
	      else
		count += S[i] - 48 ;
	    }
	}
      outfile << "Case #" << t << ": " <<  min << "\n" ;
    }
  outfile.close();
  
  return 0 ;
}
      
