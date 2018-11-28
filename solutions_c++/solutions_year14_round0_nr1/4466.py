#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <cctype>

using namespace std;

int T, R1, R[20];

int main(){

    int z, i,j, s, x;

    scanf("%d", &T);

    for (z=1; z<=T; z++) {
        memset(R, 0, sizeof(R));
        scanf("%d", &R1);
        R1--;
        for(i=0; i<4; i++){
            for (j=0; j<4; j++){
                scanf("%d", &x);
                if (i==R1)
                    R[x] ++;
            }
        }
        scanf("%d", &R1);
        R1--;
        for(i=0; i<4; i++){
            for (j=0; j<4; j++){
                scanf("%d", &x);
                if (i==R1)
                    R[x] ++;
            }
        }

        s = -1;
        for(i=0; i<20; i++){
            if(R[i]>=2)
                if(s==-1)
                    s=i;
                else
                    s=30;
        }
        printf("Case #%d: ", z);
        if(s==-1)
            printf("Volunteer cheated!\n");
        else if(s==30)
            printf("Bad magician!\n");
        else
            printf("%d\n", s);
    }

    return 0;
}
