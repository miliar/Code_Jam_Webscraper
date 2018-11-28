#include <cstdio>
//#include <cstdlib>
#include <iostream>

using namespace std;

int main () {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t, T, N, i,m[1005], ans1, ans2, mx;
    scanf("%d",&T);

    for ( t = 1 ; t <= T ; t ++ ) {
        scanf("%d",&N);
        for ( i = 0 ; i < N ; i ++ )
            scanf("%d",&m[i]);

        //ans1
        for ( ans1 = i = 0 ; i < N-1 ; i ++ ) {
            if ( m[i] > m[i+1] )
                ans1 += m[i]-m[i+1];
        }

        //ans2
        for ( mx = i = 0 ; i < N-1 ; i ++ ) {
            if ( m[i] > m[i+1] )
                mx = max(mx,m[i]-m[i+1]);
        }
        for ( ans2 = i = 0 ; i < N-1 ; i ++ ) {
            ans2 += min(mx,m[i]);
        }


        printf("Case #%d: %d %d\n",t,ans1,ans2);
    }
    //system("pause");
    return 0;
}
