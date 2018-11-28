#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
	
    
   	int N, T;
   	int l, x, c, r;
   	char L[10];
   	
//	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
//	freopen("A-sample.in","rt",stdin);
	freopen("A.out","wt",stdout);
   	
	scanf("%d",&T);
	for (int l = 0; l < T; l++) {
        scanf("%d",&N);
        if (N==0)
			printf("Case #%d: INSOMNIA\n",l+1);
        else {
        	memset(L,0,10); c=0; r=0;
        	while(c!=10) {
        		x=(r+=N);
        		while (x>0) {
        			if (L[x%10]==0) {
        				c++;
        				L[x%10]=1;
					}
					x/=10;
				}
				
			}
        	
        	
			printf("Case #%d: %d\n",l+1,r);
		}
    }

    //system("PAUSE");
    return EXIT_SUCCESS;
}
