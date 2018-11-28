#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 100

//int A[MAXN+1][MAXN+1];

vector < vector<int> > A;

int T, n, m, x;

int main( ) {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf ( "%d", &T );
    
    for ( int t = 1; t <= T; ++t ) {
    
        scanf ( "%d %d", &n, &m );
    
        A.clear();
    
        A.resize(n);
    
        for ( int i = 0; i < n; ++i )
            for ( int j = 0; j < m; ++j ) {
                scanf ( "%d", &x );
                A[i].push_back( x );
                //scanf ( "%d", &A[i][j] );
            }

        while ( true ) {
  
            int idx = 0;
            
            while ( idx < A.size() ) {
            
                  if ( A[idx].empty() ) {
                     A.erase( A.begin()+idx );
                     continue;
                  }
                  
                  ++idx;
                  
            }
        
            if ( A.empty() )
               break;

            int Minim = A[0][0];
            int minR = 0;
            int minC = 0;
            
            for ( int i = 0; i < A.size(); ++i )
                for ( int j = 0; j < A[i].size(); ++j )
                    if ( Minim > A[i][j] ) {
                       Minim = A[i][j];
                       minR = i;
                       minC = j;     
                    }
             
            int numRow = 0, numCol = 0;
            bool fRow = true, fCol = true;
            
            for ( int j = 0; j < A[minR].size(); ++j )
                if ( A[minR][j] == Minim )
                   ++numRow;
            
            if ( numRow != A[minR].size() ) {
               fRow = false;     
            }
            
            for ( int j = 0; j < A.size(); ++j )
                if ( A[j][minC] == Minim )
                   ++numCol;
             
            if ( numCol != A.size() )
               fCol = false;
            
            if ( fRow == false && fCol == false ) {
               //printf ( "Case #%d: NO\n", t );
               break;
            }
            
            if ( fRow ) {
               A.erase( A.begin() + minR );    
            }else if ( fCol ) {
               for ( int j = 0; j < A.size(); ++j )
                   A[j].erase( A[j].begin() + minC );               
            }
        
        }//end of while
        
        if ( A.size() == 0 ) {
           printf ( "Case #%d: YES\n", t );           
        }else {
           printf ( "Case #%d: NO\n", t );                 
        }
        
    }

    return 0;
   
}
