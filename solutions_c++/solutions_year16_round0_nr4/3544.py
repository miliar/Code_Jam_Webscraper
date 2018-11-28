#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
	
    
   	int T;
   	int K, C, S;
   	int l, c;
   	
   	
	freopen("D-small-attempt0.in","rt",stdin);
//	freopen("D-large.in","rt",stdin);
//	freopen("D-sample.in","rt",stdin);
	freopen("D.out","wt",stdout);
   	
	scanf("%d",&T);
	for (int l = 0; l < T; l++) {
        scanf("%d %d %d\n",&K, &C, &S);
        if (S<K)
		  printf("Case #%d: IMPOSSIBLE",l+1);
		else {
		  	printf("Case #%d:",l+1);
          	for (c=1;c<=K;c++) 
		  		printf(" %d",c);
		}
	  	printf("\n");
    }

    //system("PAUSE");
    return EXIT_SUCCESS;
}
