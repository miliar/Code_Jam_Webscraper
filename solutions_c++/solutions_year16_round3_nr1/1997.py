#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 30

typedef struct partie{
    int num;
    char c;
}partie_t;

int cmp(const void *a, const void *b){
    return ((partie_t *)b)->num - ((partie_t *)a)->num;
}

int main(void){
    int t, n, i, caso = 1;
    partie_t parties[MAX];

    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        memset(parties, 0, sizeof(parties));
        for(i = 0; i < n; i++){
            scanf("%d", &parties[i].num);
            parties[i].c = 'A' + i;
        }
        printf("Case #%d: ", caso++);
        qsort(parties, n, sizeof(partie_t), cmp);
        while(parties[0].num){
//printf("(");
//for(i = 0; i < n; i++) printf("%d ", parties[i].num);
//printf(")");
            printf("%c", parties[0].c);
            if(parties[0].num == parties[1].num && parties[2].num != 1){
                printf("%c ", parties[1].c);
                parties[1].num--;
            }
            else printf(" ");
            parties[0].num--;
            qsort(parties, n, sizeof(partie_t), cmp);
        }
        printf("\n");
    }

    return 0;
}
