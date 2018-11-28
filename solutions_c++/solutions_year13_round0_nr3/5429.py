#include <stdio.h>
#include <string.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main(){
  int t, i, cnt, mem, mem2, mem3, k;
  long long int mema, memb, j;
  char a[100], b[100], memstr[100], memstr2[100];
  scanf ( "%d", &t );
  for ( i = 0; i < t; i++ ){
      cnt = 0;
      scanf ( "%s%s", a, b );
      mema = atoll (a), memb = atoll (b);
      for ( j = mema; j <= memb; j++ ){
          sprintf ( memstr, "%lld", j );
          mem = 0, mem2 = 0, mem3 = 0;
          for ( k = 0; k < strlen(memstr) / 2; k++ ){
              if ( memstr[k] != memstr[strlen(memstr)-k-1] ){
                  mem++;
                  break;
              }
          }
          if ( (long long int)sqrt(j) * (long long int)sqrt(j) != j ) mem2++;
          else {
              sprintf ( memstr2, "%lld", (long long int)sqrt(j) );
              for ( k = 0; k < strlen(memstr2) / 2; k++ ){
                if ( memstr2[k] != memstr2[strlen(memstr2)-k-1] ){
                    mem3++;
                    break;
                }
              }
          }
          if ( !mem && !mem2 && !mem3 ) cnt++;
      }
     printf ( "Case #%d: %d\n", i+1, cnt );
  }
 return 0;
}

