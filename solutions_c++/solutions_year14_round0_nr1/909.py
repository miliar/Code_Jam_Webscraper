#include <stdio.h>
#include <string.h>

int main() {
    int t,tc,row,i,j,v;
    int card[20];

    scanf("%d", &t);
    for(tc=1; tc<=t; ++tc) {
        int count = 0, r;
        memset(card, 0, 20*sizeof(int));

        scanf("%d", &row);
        for(i=1; i<5; ++i)
        for(j=1; j<5; ++j) {
            scanf("%d", &v);
            if(i == row) {
                card[v] = 1;
            }
        }

        scanf("%d", &row);
        for(i=1; i<5; ++i)
        for(j=1; j<5; ++j) {
            scanf("%d", &v);
            if(i == row) {
                if(card[v]) {
                    r = v;
                }
                count+= card[v] == 1;
            }
        }

        printf("Case #%d: ", tc);
        if(count == 1) printf("%d\n", r);
        else           printf("%s\n", count? "Bad magician!" : "Volunteer cheated!");
    }
    return 0;
}
