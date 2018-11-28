#include <cmath>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
     
     int T ;
     cin >> T ;
     for( int i = 0 ; i < T ; i++)
         {
          int N ;
          cin >> N ;
          int ar[10] ;
          for( int j = 0 ; j < 10 ; j++) ar[j] = 0 ;
          int count = 0 ;
          int M = N ;
         cout << "case#" << i+1<< ": " ;
         if( N == 0) {cout << "INSOMNIA" << endl  ;
                      continue ; }
          while( count != 10)
              {
                int k = M ;
                while( k != 0)
                    {
                      int p = k % 10 ;
                      if( ar[p] == 0) { ar[p] = 1 ;
                                        count++ ;}
                      k = k / 10 ;
                }
                if( count == 10) break ;
                M = M + N ;
          }
          cout << M << endl ;
     }
   
  return 0;
}