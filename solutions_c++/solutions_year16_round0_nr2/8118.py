#include <cstdio>
#include <cstring>
#define min(a,b) (((a)<(b))?(a):(b))
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        char s[128];
        int d[128][128]={};
        scanf("%s",s);
        int n = strlen(s);
        if ( s[0] == '+' ) {
            d[0][0] = 0;
            d[0][1] = 1;
        } else {
            d[0][0] = 1;
            d[0][1] = 0;
        }
        for ( int i = 1 ; i < n ; i++ ) {
            if ( s[i] == '+' ) {
                d[i][0] = min(d[i-1][0],d[i-1][1]+1);
                d[i][1] = min(d[i-1][0]+1,d[i-1][1]+2);
            } else if ( s[i] == '-' ) {
                d[i][0] = min(d[i-1][0]+2,d[i-1][1]+1);
                d[i][1] = min(d[i-1][0]+1,d[i-1][1]);
            }
        }
        printf("%d\n",min(d[n-1][0],d[n-1][1]+1));
    }
    return 0;
}
