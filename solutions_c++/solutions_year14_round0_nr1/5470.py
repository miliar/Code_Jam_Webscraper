#pragma warning( disable : 4996 ) 
#include <cstdio>
#include <iostream>

using namespace std;

int main(){

    int m1[5][5], m2[5][5];
    int c1, c2;
    int ans;
    int cc, tt;
    scanf("%d", &tt);
    for (cc = 1; cc <= tt; cc++){
        scanf("%d", &c1); c1--;
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                scanf("%d", &m1[i][j]);
            }
        }
        scanf("%d", &c2); c2--;
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                scanf("%d", &m2[i][j]);
            }
        }

        ans = -1;
        int ct = 0;
        for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++){
            if (m1[c1][i] == m2[c2][j]){
                ct++;
                ans = m1[c1][i];
            }
        }

        printf("Case #%d: ", cc);
        if (ct == 0)
            printf("Volunteer cheated!\n");
        else if (ct == 1)
            printf("%d\n", ans);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
