#include <cstdio>
#include <iostream>
#define EPS 1e-7

using namespace std;

int t, T, N;
double V, R;
double S[2], Te[2];

const int dcmp( const double &x ) { if( x < -EPS ) return -1; return x > EPS; }

int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int i;
    double ans;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {
        scanf("%d %lf %lf",&N,&V,&R);
        for ( i = 0 ; i < N ; i ++ ) {
            scanf("%lf %lf",&S[i],&Te[i]);
        }

        ans = 1e9;
        if ( N == 1 ) {
            if ( dcmp(Te[0]-R) == 0 ) {
                ans = min(ans,V/S[0]);
            }
        }
        else { // N == 2
            if ( ( dcmp(Te[0]-R) > 0 && dcmp(Te[1]-R) < 0 ) || ( dcmp(Te[0]-R) < 0 && dcmp(Te[1]-R) > 0 ) ) {
                double t2 = (Te[0]-R)*V/((Te[0]-Te[1])*S[1]);
                double t1 = (V-S[1]*t2)/S[0];
                ans = min(ans,max(t2,t1));
            }
            if ( dcmp(Te[0]-R) == 0 )
                ans = min(ans,V/S[0]);
            if ( dcmp(Te[1]-R) == 0 )
                ans = min(ans,V/S[1]);
            if ( dcmp(Te[0]-R) == 0 && dcmp(Te[1]-R) == 0 )
                ans = min(ans,V/(S[0]+S[1]));
        }

        printf("Case #%d: ",t);
        if ( dcmp(ans-1e9) == 0 ) printf("IMPOSSIBLE\n");
        else printf("%.10lf\n",ans);
    }

    return 0;
}
