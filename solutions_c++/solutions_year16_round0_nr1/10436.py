#include <stdio.h>
#include <cstdlib>

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
    
    using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main( int argc, const char* argv[] )
{
	  int t, n, prod, accu,  j;
	  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.


	  for (int i =0 ; i < t; i++ ) {
  			cin >> n ;

  			if (n == 0) {
  				cout << "Case #" << (i+1) << ": INSOMNIA" << endl ;
  			} else {
  				int tmp, ind ;
  				prod =0 ;
  				accu = 0 ;
  				int a[10] = {0}  ; 
  				while ( prod==0 ) {
  					   accu += n ;
  					   tmp = accu ;
  					   while ( tmp != 0 ) {
  					   		ind = tmp%10;
  					   		a[ind]++ ;
  					   		tmp = tmp/10;
  					   }
  					   prod = a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9] ;

  				}
  				cout << "Case #" << (i+1) << ": " << accu <<endl ;

  			}


	  }
 
	return EXIT_SUCCESS;
	
}
