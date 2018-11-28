#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
	
    
   	int T;
   	int s, l, c, r;
   	//int l, x, c, r;
   	char L[101], x;
   	
   	
//	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-large.in","rt",stdin);
//	freopen("B-sample.in","rt",stdin);
	freopen("B.out","wt",stdout);
   	
	scanf("%d",&T);
	for (int l = 0; l < T; l++) {
        scanf("%s\n",L);
        s=strlen(L);
        L[s]='+'; x=L[0]; r=0;
        for (c=1;c<=s;c++) {
        	if (L[c]!=x) {
        		r++; x=L[c];
			}
		}
		printf("Case #%d: %d\n",l+1,r);
    }

    //system("PAUSE");
    return EXIT_SUCCESS;
}
