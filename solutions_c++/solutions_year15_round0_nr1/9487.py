#include <stdio.h>

main()


{

  int T;

  scanf("%d",&T);

  for (int i = 1; i <= T; i++) {

    int m = 0;
    scanf("%d ",&m);
    
    int total = 0;
    int need = 0;
    for (int j = 0; j <= m; j++) {
      
      

      char c;
      
      scanf("%c",&c);
      int n = c - '0';

      //      if ((n < 0) or (n > 9)) continue;
      
      //  printf( "li %d, total = %d need = %d, j = %d\n",n,total,need,j);
      if (total < j) {
	need += j - total;
	total = j;
      }
      
      total += n;

    }
    printf("Case #%d: %d\n",i,need);

  }


}
