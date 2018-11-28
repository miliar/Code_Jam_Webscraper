#include <iostream>
#include <cstdio>
#include <algorithm>
#define MAX 179
#define INF 9999999
using namespace std;

long long tab[ MAX ];

int main()
{
  int t = 0, n = 0;
  long long rozm = 0;
  scanf("%d", &t);
  
  for (int i = 1; i <= t; i++) 
  {
      int mini = INF, licznik = 0;
      scanf("%lld%d", &rozm, &n);
      for (int j = 1; j <= n; j++)
	    scanf("%lld", &tab[ j ]);
      sort(tab+1,tab+n+1);
      
      if( rozm == 1 ) {
	    printf("Case #%d: %d\n", i, n);
	    continue;
      }
      
      for (int j = 1; j <= n+1; j++) {
	    mini = min(mini, licznik+n-j+1);
	    
	    //printf("Konczac gre przy %d, musze zrobic %d operacji\n", j, mini);
	    
	    if( j == n+1 )
		  break;
	    while( rozm <= tab[ j ] )
	    {
		  //printf(" ** %d\n", rozm);
		  rozm += (rozm-1);
		  licznik++;
	    }  
	    rozm += tab[ j ];
	    //printf("Zjadlem goscia nr %d, mam rozmiar %d\n", j, rozm);
      }
      printf("Case #%d: %d\n", i, mini);
  }
     
  return 0;
}
