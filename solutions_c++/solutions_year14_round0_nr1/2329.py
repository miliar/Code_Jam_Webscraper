#include<stdio.h>

int main()
{
    int t, x, y, i, j, row, choose[17], p;
    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        for(i = 0; i < 17; i++) choose[i] = 0;
        scanf("%d", &row);
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                scanf("%d", &p);
                if(i+1 == row) choose[p]++;
            }
        }
        scanf("%d", &row);
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                scanf("%d", &p);
                if(i+1 == row) choose[p]++;
            }
        }
        j = 0;
        for(i = 1; i < 17; i++)
            if(choose[i] == 2) {
                y = i;
                j++;
            }
        printf("Case #%d: ", x);
        if(j == 1) printf("%d\n", y);
        else if(j > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
