#include <cstdio>
#include <iostream>

using namespace std;



int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int a[10005];
    int t, T, ans, ans2, R, C, N, N2, i, j, c;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {

        scanf("%d %d %d",&R,&C,&N); N2 = R*C - N;

        for ( i = 0 ; i < R ; i ++ ) {
            for ( j = 0 ; j < C ; j ++ ) {
                c = 4;
                if ( i == 0 ) c--;
                if ( i == R-1 ) c--;
                if ( j == 0 ) c--;
                if ( j == C-1 ) c--;
                a[i*C+j] = c;
            }
        }
        ans = C*(R-1)+R*(C-1);
        //printf("tot =%d\n",ans);
        //for ( i = 0 ; i < R*C ; i ++ ) printf("%d%c",a[i],i%C==C-1?'\n':' ');*
        N = N2;
        while ( N-- ) {
            //printf("---\n");

            for ( c = 4 ; c >= 0 ; c -- ) {
                for ( i = 0 ; i < R*C ; i ++ ) {
                    if ( a[i] == c ) break;
                }
                if ( i != R*C ) break;
            }
            a[i] = -1;
            ans -= c;
            if ( i-C >= 0 ) a[i-C]--; // up
            if ( i%C != 0 ) a[i-1]--; // left
            if ( i+C < R*C ) a[i+C]--; // down
            if ( i%C != C-1 ) a[i+1]--; // right
            //for ( i = 0 ; i < R*C ; i ++ ) printf("%d%c",a[i],i%C==C-1?'\n':' ');
        }



        for ( i = 0 ; i < R ; i ++ ) {
            for ( j = 0 ; j < C ; j ++ ) {
                c = 4;
                if ( i == 0 ) c--;
                if ( i == R-1 ) c--;
                if ( j == 0 ) c--;
                if ( j == C-1 ) c--;
                a[i*C+j] = c;
            }
        }
        ans2 = C*(R-1)+R*(C-1);
        /*printf("tot =%d\n",ans);
        for ( i = 0 ; i < R*C ; i ++ ) printf("%d%c",a[i],i%C==C-1?'\n':' ');*/
        N = N2;
        bool flag = false;
        while ( N-- ) {
            //printf("---\n");
            int cnt = 0;
            for ( c = 4 ; c >= 0 ; c -- ) {
                for ( i = 0 ; i < R*C ; i ++ ) {
                    if ( a[i] == c ) {
                        if ( flag == false ) {
                            if ( cnt == 0 ) cnt ++;
                            else break;
                        }
                        else break;
                    }
                }
                if ( i != R*C ) break;
            }
            a[i] = -1;
            ans2 -= c;
            if ( i-C >= 0 ) a[i-C]--; // up
            if ( i%C != 0 ) a[i-1]--; // left
            if ( i+C < R*C ) a[i+C]--; // down
            if ( i%C != C-1 ) a[i+1]--; // right
            //for ( i = 0 ; i < R*C ; i ++ ) printf("%d%c",a[i],i%C==C-1?'\n':' ');
            flag = true;
        }
        //printf("%d %d\n",ans,ans2);


        printf("Case #%d: %d\n",t,min(ans,ans2));

    }
    return 0;

}
