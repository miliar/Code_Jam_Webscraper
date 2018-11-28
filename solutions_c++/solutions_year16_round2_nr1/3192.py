#include<iostream>

#include<vector>
#include<algorithm>
#include<string>

using namespace std ;

int main() 
   {
    int T ;
    cin >> T ;
    for( int i = 0 ; i < T ; i++ ) 
	{
	  string s ;
          cin >> s ;
	  int ar[26] ;
          for( int j = 0 ; j < 26 ; j++)
		{
		  ar[j] = 0 ;
		}
	  vector<int> num ;
          int count = s.length() ;
          for( int j = 0 ; j < s.length() ; j++)
	     {
	       int c = s[j] - 'A' ;
	       ar[c]++ ;
             }
	  while( count != 0 )
	      {

if( ar[25] != 0 ) { ar[25]-- ;
		    ar[4]-- ;
		    ar[17]-- ;
		    ar[14]-- ;
		   num.push_back( 0 ) ;
		    count -= 4 ;
		    continue ; } 

if( ar[22] != 0 ) { ar[22]-- ;
		    ar[19]-- ;
		    ar[14]-- ;
		    count -= 3 ;
		 num.push_back( 2 ) ;
		    continue ;
		   }
if( ar[23] != 0 ) { ar[23]-- ;
		    ar[8]-- ;
		    ar[18]-- ;
			count -= 3 ;
		 num.push_back( 6 ) ;
		   continue ;
		}

if( ar[6] != 0 ) { ar[6]-- ;
		   ar[4]-- ;
		   ar[8]-- ;
		   ar[7]-- ;
		   ar[19]-- ;
		  count -= 5 ;
		 num.push_back( 8 ) ;
			continue ;
		}

if( ar[18] != 0 ) { ar[18]-- ;
		    ar[4] -= 2 ;
		    ar[21]-- ;
		    ar[13]-- ;
count -= 5 ;
num.push_back( 7 ) ;
		 continue ;
		  }

if( ar[21] != 0 ) { ar[21]-- ;
		    ar[5]--;
		ar[8]--;
		ar[4]--;
count -= 4 ;
num.push_back( 5 ) ;
			continue;
		}
if( ar[5] != 0 ) { ar[5]-- ;
		   ar[14]-- ;
		   ar[20]-- ;
		   ar[17]-- ;
count -= 4 ;
num.push_back( 4 ) ;
		  continue ;
		}


if( ar[14] != 0 ) { ar[14]-- ;
		    ar[13]-- ;
			ar[4]-- ;
count -= 3 ;
num.push_back( 1 ) ;
		   continue ;
		}

if( ar[13] != 0 ) { ar[13] -= 2 ;
		    ar[8]-- ;
		    ar[4]-- ;
count -= 4 ;
num.push_back( 9 ) ;
			 continue ;
		}

if( ar[4] != 0 ) { ar[4] -= 2 ;
		   ar[19]-- ;
		   ar[7]-- ;
		   ar[17]-- ;
count -= 5 ;
num.push_back( 3 ) ;
		  continue ;
		}

}

		   





	sort( num.begin() , num.end() ) ;
	cout << "Case #" << i + 1 << ": " ;
	for( int j = 0 ; j < num.size() ; j++)
		{  cout << num[j] ; }
	 cout << endl ;
 }
	 return 0 ;
	}
