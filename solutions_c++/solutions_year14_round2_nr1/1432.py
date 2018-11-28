#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>
#include <math.h>
#include <vector>
#include <algorithm>

#define MIN(a,b) (a < b ? a : b)

using namespace std;

int main( void ) {
     const int Max = 100;
     char str[Max][Max+1];
     
     int nCase, n = 1;
     scanf("%i", &nCase);
     
     while( nCase-- ) {
          int nmove = 0, possible = 1;
          
          int N;                             /* read Number of strings */
          scanf("%i", &N);
          
          for( int i = 0; i < N; i++ )        /* read a string */
               scanf("%s", str[i]);
         
         vector< vector<pair<char, int> > > v;
         
         for( int i = 0; i < N; i++ ) {
               vector< pair<char, int> > al;
               
               for( int j = 0; j < strlen(str[i]); ) {
                    char c = str[i][j];
                    int cc = 1;
                    
                    j +=1;
                    while( (j < strlen(str[i])) && (str[i][j] == str[i][j-1]) ) {
                         j++;
                         cc++;
                    }
                    al.push_back( make_pair(c, cc) );
               }
               
               v.push_back(al);
         }
     
         for( int i = 1; i < N; i++ )
               if( v[i].size() != v[0].size() ) {
                    possible = 0;
                    break;
               }
         
//          for( int i = 0; i < N; i++ ) {
//               for( int j = 0; j < v[i].size(); j++ )
//                    printf("(%c %i) ", v[i][j].first, v[i][j].second );
//               printf("\n");
//          }
//          
          if( !possible ) {
               printf("Case #%i: Fegla Won\n", n++);
          } else {
               
               for( int i = 0; i < v[0].size(); i++ ) {
                    
                    int min = INT_MAX;
                    for( int j = 0; j < N; j++ ) {
                         int cnt = 0;
                         
                         for( int c = 0; c < N; c++ ) {
                              if( c == j ) continue;
                              if( v[j][i].first != v[c][i].first ){
                                   possible = 0;
                                   break;
                              }
                              else cnt += fabs(v[j][i].second-v[c][i].second);
                         }
                         
                         min = MIN(min , cnt);
                    }
                    
                    if( !possible ) break;
                    else nmove += min; 
               }
               
               if( possible )
                    printf("Case #%i: %i\n", n++, nmove);
               else
                   printf("Case #%i: Fegla Won\n", n++); 
          }
     
     }
     
     return 0;
}
