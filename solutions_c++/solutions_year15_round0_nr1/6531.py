#include<stdio.h>
int main()
{
    int T,sm,i,j,f,stand;
    char a[1005];
    scanf("%d",&T);
    for(i = 1; i <= T; i++) {
        f = 0;stand = 0;
        scanf("%d %s",&sm,a);
        for(j = 0; j <= sm; j++) {
            if(stand < j) { /*too shy, need to invite*/
                f = f + (j - stand);
                stand = j + (a[j] - '0') ;
            }
            else {
            	stand = stand + (a[j] - '0');
			}
        } 
        printf("Case #%d: %d\n",i,f);
    }
    return 0;
}
