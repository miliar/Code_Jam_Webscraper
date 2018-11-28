#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<fstream>

#define lld long long 
#define llu unsigned long long //No need to write int ahead of long long 

using namespace std ;


int main()
{
  
  int M[5][5], count[3] = {0}, temp, t, i, j, L, X, k, T, neg ;//i - 2, j - 3, k - 4
  M[1][1] = 1 ;
  for( i = 1 ; i < 5 ; i++ )
    {
      for( j = 1 ; j < 5 ; j++ )
	{
	  if( i != 1 && i == j )
	    M[i][j] = -1 ;
	  else if( i == 1 && j > 1 )
	    M[i][j] = j ;          //can also store 103+j for ASCII value
	  else if( j == 1 && i > 1 )
	    M[i][j] = i ;
	}
    }
  M[2][3] = 4 ; M[2][4] = -3 ; M[3][2] = -4 ; M[3][4] = 2 ; M[4][2] = 3 ; M[4][3] = -2 ;
  char A[10001], temp_c ;
  ifstream infile ;       // input file object
  ofstream outfile;       // output file object
  infile.open ("C-small-attempt1.in") ; 
  infile >> T ;
  outfile.open( "C-small-attempt1.out") ;  
  for( t = 1 ; t <= T ; t++ )
    {
      infile >> L >> X ;
      for( i = 0 ; i < L ; i++ )
	infile >> A[i] ;
      if( X > 1 )
	{
	  for( j = i ; j < i + (X-1) * L ; j++ )
	    {
	      for( k = 0 ; k < L ; k++ )
		{
		  temp_c = A[k] ;
		  A[j] = temp_c ;
		  //k++ ;
		  j++ ;
		}
	      j = j - 1 ;
	    }
	}
      /*cout << "Array\n" ;
      for( i = 0 ; i < L * X ; i++ )
	cout << A[i] ;
      cout << "\n" ;*/
      
      for( i = 0 ; i < 3 ; i++ )
	count[i] = 0 ;       //0 for i, 1 for j, 2 for k
      
      for( i = 0 ; i < L * X ; i++ )
	{
	  if( count[0] == 0 )//Search for i
	    {
	      if( i == L * X )
		{
		  outfile << "Case #" << t << ": " << "NO\n" ;
		  break ;
		}
	      else if( i == 0 && A[i] == 'i' )
		{
		  count[0] = 1 ;
		  i = i + 1 ;
		}
	      else
		{
		  temp = A[i] - 103 ;
		  neg = 1 ;
		  for( j = i + 1 ; j < L * X ; j++ )
		    {
		      if( M[temp][A[j]-103] * neg == 2 )
			{
			  count[0] = 1 ;
			  i = j + 1 ;
			  break ;
			}
		      temp = M[temp][A[j]-103] * neg ;          //multiplied neg
		      if( temp < 0 )
			{
			  neg = -1 ;
			  temp = -temp ;
			}
		      else
			neg = 1 ;
		    }
		  if( j == L * X && count[0] == 0 )
		    {
		      outfile << "Case #" << t << ": " << "NO\n" ;
		      break ;
		    }
		  
		}
	    }
	  
	  if( count[0] == 1 && count[1] == 0 )//Search for j
	    {
	      if( i == L * X )
		{
		  outfile << "Case #" << t << ": " << "NO\n" ;
		  break ;
		}
	      else if( A[i] == 'j' )
		{
		  count[1] = 1 ;
		  i += 1 ;
		}
	      else
		{
		  temp = A[i] - 103 ;
		  neg = 1 ;
		  for( j = i + 1 ; j < L * X ; j++ )
		    {
		      if( M[temp][A[j]-103] * neg == 3 )
			{
			  count[1] = 1 ;
			  i = j + 1 ;                        //Newly added
			  break ;
			}
		      temp = M[temp][A[j]-103] * neg ;  //multiplied neg
		      if( temp < 0 )
			{
			  neg = -1 ;
			  temp = -temp ;
			}
		      else
			neg = 1 ;
		    }
		  if( j == L * X && count[1] == 0 )
		    {
		      outfile << "Case #" << t << ": " << "NO\n" ;
		      break ;
		    }
		}
	    }
	  
	  if( count[0] == 1 && count[1] == 1 && count[2] == 0 )//Search for k
	    {
	      if( i == L * X )
		{
		  outfile << "Case #" << t << ": " << "NO\n" ;
		  break ;
		}
	      else if( A[i] == 'k' && i == L * X - 1 )
		{
		  count[2] = 1 ;
		  //i += 1 ;
		}
	      
	      else
		{
		  temp = A[i] - 103 ;
		  neg = 1 ;
		  for( j = i + 1 ; j < L * X ; j++ )
		    {
		      if( M[temp][A[j]-103] * neg == 4 && j == L * X - 1 )
			{
			  count[2] = 1 ;
			  i = j ;
			  break ;
			}
		      temp = M[temp][A[j]-103] * neg ;  //multiplied neg
		      if( temp < 0 )
			{
			  neg = -1 ;
			  temp = -temp ;
			}
		      else
			neg = 1 ;
		    }
		  if( j == L * X && count[2] == 0 )
		    {
		      outfile << "Case #" << t << ": " << "NO\n" ;
		      break ;
		    }
		}
	    }
	  if( count[1] == 1 && count[2] == 1 && count[0] == 1 )
	    {
	      break ;
	    }
	}
      if( count[1] == 1 && count[2] == 1 && count[0] == 1 && i < L * X - 1 )
	{
	  //cout << "t and i " << t << " " << i << "\n" ;
	  outfile << "Case #" << t << ": " << "NO\n" ;
	}
      if( count[1] == 1 && count[2] == 1 && count[0] == 1 && i == L * X - 1 )
	{
	  outfile << "Case #" << t << ": " << "YES\n" ;
	}
    }
  return 0 ;
  
}
	  
