#include <stdio.h>
#include <queue>
using namespace std;
char name[2][10]={"RICHARD","GABRIEL"};
int main()
{
    int T,x,r,c,ncase=0;
    scanf("%d",&T);
    while(T--) {
        scanf("%d%d%d",&x,&r,&c);
        int ans = 0;
        if(r*c%x!=0) {
            ans = 0;
        } else {
            ans = 1;
            if(x==3 && r*c==3) ans = 0;
            if(x==4 && r*c<12) ans = 0;
        }
        printf("Case #%d: %s\n", ++ncase, name[ans]);
    }

	return 0;
}
/*
10
1 11
1 12
1 13
1 14
1 15
1 16
1 17
1 18
1 19
1 20
*/
