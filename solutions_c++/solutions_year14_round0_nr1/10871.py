#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>

using namespace std;

int t, r1, r2, aux, qt, resp;
int c1[5][5], c2[5][5];

int main()
{

    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &t);

    for(int i = 1; i <= t; i++){
        scanf("%d", &r1);
        for(int j = 1; j <= 4; j++){
            for(int k = 1; k <= 4; k++){
                scanf("%d", &c1[j][k]);
            }
        }

        scanf("%d", &r2);
        for(int j = 1; j <= 4; j++){
            for(int k = 1; k <= 4; k++){
                scanf("%d", &c2[j][k]);
            }
        }

        qt = 0;
        aux = 0;
        resp = 0;
        for(int j = 1; j <= 4; j++){
            aux = c1[r1][j];
            for(int k = 1; k <= 4; k++){
                if(aux==c2[r2][k]){
                    resp = aux;
                    qt++;
                }
            }
        }

        printf("Case #%d: ", i);

        if(qt == 0){
            printf("Volunteer cheated!\n");
        } else if (qt > 1){
            printf("Bad magician!\n");
        } else {
            printf("%d\n", resp);
        }
    }

    return 0;
}
