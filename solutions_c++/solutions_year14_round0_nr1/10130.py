#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int test;
    int k = 0;
    scanf ( "%d", &test );
    while ( k < test){
    int as1,as2;
    int a[4][4],b[4][4];
    int a1[4],b1[4];
    scanf ( "%d", &as1);
    for ( int i = 0; i < 4; i++ ){
        for ( int j = 0; j < 4; j++){
            scanf ( "%d", &a[i][j]);
            if ( i+1 == as1 ){
                a1[j] = a[i][j];
            }
        }
    }

    scanf ( "%d", &as2);
    for ( int i = 0; i < 4; i++ ){
        for ( int j = 0; j < 4; j++){
            scanf ( "%d", &b[i][j]);
            if ( i+1 == as2 ){
                b1[j] = b[i][j];
            }
        }
    }
    int u = 0;
    int y;
    for ( int i = 0; i < 4; i++){
        for ( int j = 0; j < 4; j++ ){
            if ( a1[i] == b1[j]){
             y = a1[i];
              u++;
            }
        }
    }
    if ( u == 0){
        printf ( "Case #%d: Volunteer cheated!\n",k+1);
    }else if ( u > 1 ){
        printf ( "Case #%d: Bad magician!\n",k+1);
    }else {
        printf ( "Case #%d: %d\n", k+1,y);
    }
    k++;
    }
    return 0;
}
