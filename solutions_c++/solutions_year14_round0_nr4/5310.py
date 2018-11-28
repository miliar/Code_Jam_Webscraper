#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main () {
    int T;
    scanf("%d",&T);
    int N;
    double Naomi[10];
    double Ken[10];
    for ( int w = 1; w <= T; w++ ) {
        memset(Naomi,0,sizeof(Naomi));
        memset(Ken,0,sizeof(Ken));
        scanf("%d",&N);
        for ( int i = 0; i < N; i++) {
            scanf("%lf",&Naomi[i]);
        }
        sort(Naomi,Naomi+N);
        for ( int i = 0; i < N; i++) {
            scanf("%lf",&Ken[i]);
        }
        sort(Ken,Ken+N);
        
        int War = 0, i = 0, j = 0;
        
        for ( i; i < N; i++) {
            for ( j; j < N; j++) {
                if ( Ken[j] > Naomi[i] ) {
                    j++;
                    break;
                } else if ( j == (N-1) ) {
                    War++;
                }
            }
            
            if ( j >= N) break;
        }
        
        War += N - i - 1;
        
        int DWar = 0, BlocksJ = N;
        i = 0;
        j = 0;
        
        while ( i < N && j < BlocksJ) {
            if ( Naomi[i] > Ken[j] ) {
                DWar++;
                i++;
                j++;
            } else {
                i++;
                BlocksJ--;
            }
            
            if ( j >= BlocksJ ) break;
        }
        
        if ( i != N ) DWar += N - i - 1;
        
        printf("Case #%d: %d %d\n",w,DWar,War);
    }
    return 0;   
}