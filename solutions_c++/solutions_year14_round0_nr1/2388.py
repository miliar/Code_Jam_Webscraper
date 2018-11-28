#include <cstdio>
#include <iostream>
#include <cstring>
#define MAX 4

using namespace std;

int a[MAX][MAX];
int hash[MAX];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int t, cc = 1;
    scanf("%d", &t);

    while( t --){
        int choose = 0;
        memset( a, 0, sizeof(a));
        memset( hash, 0, sizeof(hash));
        scanf("%d", &choose);
//        cin >> choose;

        for ( int i = 0; i < 4; i ++){
            for ( int j = 0; j < 4; j ++){
                scanf("%d", &a[i][j]);
//                cin >> a[i][j];
            }
        }

        for ( int i = 0; i < 4; i ++){
            hash[i] = a[choose - 1][i];
        }

        scanf("%d", &choose);
//        cin >> choose;

        for ( int i = 0; i < 4; i ++){
            for ( int j = 0; j < 4; j ++){
                scanf("%d", &a[i][j]);
//                cin >> a[i][j];
            }
        }

        int count = 0, ans = 0;
        for ( int i = 0; i < 4; i ++){
            for ( int j = 0; j < 4; j ++){
                if ( hash[j] == a[choose - 1][i]){
                    ans = a[choose - 1][i];
                    count ++;
                }
            }
        }

        if ( 1 == count){
            printf("Case #%d: %d\n", cc, ans);
        }
        else if ( 0 == count){
            printf("Case #%d: Volunteer cheated!\n", cc);
        }
        else{
            printf("Case #%d: Bad magician!\n", cc);
        }

        cc ++;
    }

    return 0;
}
