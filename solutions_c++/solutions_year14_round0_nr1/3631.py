#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;

int A[4][4], B[4][4];
int c[17];

int main()
{
    int k;
    scanf("%d",&k);
    for(int t=0; t<k; t++) {

        int g1,g2;
        scanf("%d", &g1); g1--;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                scanf("%d", &A[i][j]);
                if( i == g1 ) c[ A[i][j] ]++;
            }
        }
        scanf("%d", &g2); g2--;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++){
                scanf("%d", &B[i][j]);
                if( i == g2 ) c[ B[i][j] ]++;
            }
        }

        //for(int i=0; i<=16; i++) printf("%d ", c[i]);
        
        bool suc = false;
        int ans = 0;
        for(int i=1; i<=16; i++) {
            if( c[i] == 2 ) {
                if( ans > 0 ){
                    printf("Case #%d: Bad magician!\n", t+1);
                    suc = false;
                    break;
                }
                ans = i;
                suc = true;
            }
        }

        if( ans == 0 ) {
            printf("Case #%d: Volunteer cheated!\n", t+1);
        }
        else if( suc ) {
            printf("Case #%d: %d\n", t+1, ans );
        }

        for(int i=0; i<17; i++) c[i] = 0;
        
    }

    return 0;
}
