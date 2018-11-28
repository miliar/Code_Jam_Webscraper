#include <algorithm>
#include <cstdio>
using namespace std;
#define REP(i,b) for ( int i = 0; i < int(b); ++i )
#define FOR(i,a,b) for ( int i = int(a); i <= int(b); ++i )

int arr1[5], arr2[5];

int main( ) {
  int caseCnt, r1, r2;
  scanf("%d", &caseCnt);
  FOR( caseNr, 1, caseCnt ) {
    scanf("%d", &r1);
    FOR( r, 1, 4 ) {
      REP( c, 4 ) {
        if ( r == r1 )
          scanf("%d", &arr1[c]);
        else
          scanf("%*d");
      }
    }
    scanf("%d", &r2);
    FOR( r, 1, 4 ) {
      REP( c, 4 ) {
        if ( r == r2 )
          scanf("%d", &arr2[c]);
        else
          scanf("%*d");
      }
    }
    sort( arr1, arr1+4 );
    sort( arr2, arr2+4 );
    int common = 0, num;
    for ( int i = 0, j = 0; i < 4 && j < 4; ) {
      if ( arr1[i] > arr2[j] )
        ++j;
      else if ( arr1[i] < arr2[j] )
        ++i;
      else {
        ++common;
        num = arr1[i];
        ++i, ++j;
      }
    }
    printf("Case #%d: ", caseNr);
    if ( !common )
      printf("Volunteer cheated!\n");
    else if ( common > 1 )
      printf("Bad magician!\n");
    else
      printf("%d\n", num);
  }
  return 0;
}