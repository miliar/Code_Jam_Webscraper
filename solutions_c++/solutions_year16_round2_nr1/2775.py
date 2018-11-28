#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 2123

int cmp( const void *a, const void *b){
    return *(int *)a - *(int *)b;
}

int main(void){
    int i, t, l[100], num[MAX], cas = 1;
    char c;

    scanf("%d\n", &t);
    while(t--){
        memset(l, 0, sizeof(l));
        while(scanf("%c", &c), c!= '\n') l[c]++;
        i = 0;

        if(l[90])
            while(l[90]--){
                num[i++] = 0;
                l[69]--; l[82]--; l[79]--;
            }
        if(l[87])
            while(l[87]--){
                num[i++] = 2;
                l[84]--; l[79]--;
            }
        if(l[85])
            while(l[85]--){
                num[i++] = 4;
                l[70]--; l[79]--; l[82]--;
            }
        if(l[88])
            while(l[88]--){
                num[i++] = 6;
                l[83]--; l[73]--;
            }
        if(l[71])
            while(l[71]--){
                num[i++] = 8;
                l[69]--; l[73]--; l[72]--; l[84]--;
            }
        if(l[84])
            while(l[84]--){
                num[i++] = 3;
                l[72]--; l[82]--; l[69]-=2;
            }
        if(l[70])
            while(l[70]--){
                num[i++] = 5;
                l[73]--; l[86]--; l[69]--;
            }
        if(l[83])
            while(l[83]--){
                num[i++] = 7;
                l[69]-=2; l[86]--; l[78]--;
            }
        if(l[73])
            while(l[73]--){
                num[i++] = 9;
                l[78]-=2; l[69]--;
            }
        while(l[79]--) num[i++] = 1;


        qsort(num, i, sizeof(int), cmp);
        printf("Case #%d: ", cas++);
        for(int k = 0; k < i; k++) printf("%d", num[k]);
        printf("\n");
    }
    return 0;
}
