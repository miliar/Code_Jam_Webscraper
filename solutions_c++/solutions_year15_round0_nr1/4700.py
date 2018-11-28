#include"stdio.h"
#include"stdlib.h"

int main(){
    int t;
    char num[10000];
    int s;
    scanf("%d", &t);
    for(int i=0;i<t;i++){
        scanf("%d%s", &s, num);
        int add = 0;
        int sum = num[0]-(int)'0';
        for(int j=1;j<=s;j++){
            if((sum+add)<j)add += j-(sum+add);
            sum += num[j]-(int)'0';

        }
        printf("Case #%d: %d\n", i+1, add);
    }
}
