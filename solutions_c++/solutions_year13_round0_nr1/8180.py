#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
    int t,i,j,k;
    string s;
    
    freopen ("inp.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf("%d", &t);
    
    for ( k = 1; k <= t; k++ ) {
          vector <string> v;
          for ( i = 0; i < 4; i++ ) {
              cin >> s;
              v.push_back(s);
          }
          int a[4],b[4],a1[4],b1[4],dot=0,T1=-1,T2=-1;
          
          memset(a, 0, sizeof(a));
          memset(b, 0, sizeof(b));
          memset(a1, 0, sizeof(a1));
          memset(b1, 0, sizeof(b1));
          
          int dig1a=0,dig1b=0,dig2a=0,dig2b=0;
         
          if ( v[0][0] == 'X' ) dig1a++;
          if ( v[0][0] == 'O' ) dig1b++;
          if ( v[1][1] == 'X' ) dig1a++;
          if ( v[1][1] == 'O' ) dig1b++;
          if ( v[2][2] == 'X' ) dig1a++;
          if ( v[2][2] == 'O' ) dig1b++;
          if ( v[3][3] == 'X' ) dig1a++;
          if ( v[3][3] == 'O' ) dig1b++;
    
          if ( v[0][3] == 'X' ) dig2a++;
          if ( v[0][3] == 'O' ) dig2b++;
          if ( v[1][2] == 'X' ) dig2a++;
          if ( v[1][2] == 'O' ) dig2b++;
          if ( v[2][1] == 'X' ) dig2a++;
          if ( v[2][1] == 'O' ) dig2b++;
          if ( v[3][0] == 'X' ) dig2a++;
          if ( v[3][0] == 'O' ) dig2b++;
          
          if ( dig1a == 4 ) {
             printf("Case #%d: X won\n", k);
             continue;
          }
          if ( dig2a == 4 ) {
             printf("Case #%d: X won\n", k);
             continue;
          }
          if ( dig1b == 4 ) {
             printf("Case #%d: O won\n", k);
             continue;
          }
          if ( dig2b == 4 ) {
             printf("Case #%d: O won\n", k);
             continue;
          }
             
          for ( i = 0; i < 4; i++ ) {
              for ( j = 0; j < 4; j++ ) {
                  if ( v[i][j] == 'O' ) {
                     b[i]++;
                     b1[j]++;
                  }
                  else if ( v[i][j] == 'X' ) {
                       a[i]++;
                       a1[j]++;
                  }
                  else if ( v[i][j] == '.' ) dot++;
                  else {
                       T1 = i;
                       T2 = j;
                  }
              }
          }
          
          for ( i = 0; i < 4; i++ ) {
              if ( a[i] == 4 ) {
                 printf("Case #%d: X won\n", k);
                 goto ab;
              }
              else if ( b[i] == 4 )  {
                   printf("Case #%d: O won\n", k);
                   goto ab;
              }
          }
          for ( i = 0; i < 4; i++ ) {
              if ( a1[i] == 4 ) {
                 printf("Case #%d: X won\n", k);
                 goto ab;
              }
              else if ( b1[i] == 4 ) {
                    printf("Case #%d: O won\n", k);
                    goto ab;
              }
          }
          if ( T1 == -1 && T2 == -1 ) {
             if ( dot != 0 ) printf("Case #%d: Game has not completed\n", k);
             else printf("Case #%d: Draw\n", k);
          }
          
          else {
               if ( a[T1] == 3 ) printf("Case #%d: X won\n", k);
               else if ( b[T1] == 3 ) printf("Case #%d: O won\n", k);
               else if ( a1[T1] == 3 ) printf("Case #%d: X won\n", k);
               else if ( b1[T1] == 3 ) printf("Case #%d: O won\n", k);
               else if ( T1 == T2 ) {
                       if ( dig1a == 3 ) printf("Case #%d: X won\n", k);
                       else if ( dig1b == 3 ) printf("Case #%d: O won\n", k);
                       else {
                            if ( dot != 0 ) printf("Case #%d: Game has not completed\n", k);
                            else printf("Case #%d: Draw\n", k);
                       }
               }
               else if ( (T1 == 0 && T2 == 3) || (T1 == 3 && T2 == 0) || (T1 == 1 && T2 == 2) || (T1 == 2 && T2 == 1) ) {
                      if ( dig2a == 3 ) printf("Case #%d: X won\n", k);
                      else if ( dig2b == 3 ) printf("Case #%d: O won\n", k);
                      else {
                           if ( dot != 0 ) printf("Case #%d: Game has not completed\n", k);
                           else printf("Case #%d: Draw\n", k);
                      }
               }
               else {
                    if ( dot != 0 ) printf("Case #%d: Game has not completed\n", k);
                    else printf("Case #%d: Draw\n", k);
               }
               ab: { }
          }     
    }
    
    return 0;
}      
