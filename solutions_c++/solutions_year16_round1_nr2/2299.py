#include <cmath>
#include <cstdio>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

bool fun1( int a , int b)
    {
      return a < b ;
}



int main() {
  
    int T ;
    cin >> T ;
    for( int i = 0 ; i < T ; i++)
        {
        int N ;
        cin >> N ;
        int ar[2505] ;
        cout << "Case #" << i + 1 << ": " ;
        for( int j = 0 ; j < 2505 ; j++) ar[j] = 0 ;
        int max = 0 ;
        for( int j = 0 ; j < 2 * N - 1 ; j++)
            {
              for( int k = 0 ; k < N ; k++)
                  {
                   int t ;
                  cin >> t ;
                  if( t > max) max = t ;
                  ar[t]++;
              }
        }
        vector<int> newrow ;
        for( int j = 0 ; j <= max; j++)
            {
              if( ar[j] % 2 == 1) newrow.push_back( j ) ;
        }
        sort( newrow.begin() , newrow.end() , fun1) ;
        for( int j = 0 ; j < N ; j++)
            {
             cout << newrow[j] << " " ;
        }
        cout << endl ;
    }
    
    
    
  return 0;
}