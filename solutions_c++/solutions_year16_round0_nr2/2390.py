#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void reverse(char * pancake, int end){
    char tmp[121];
    //printf("[%s] %d\n", pancake, end);
    for(int i=0;i<end;i++){
        char c = '-';
        if(pancake[i] == '-')c = '+';
        tmp[i] = c;
    }
    for(int i=0;i<end;i++){
        pancake[i] = tmp[end - 1 - i];
    }
    //printf("[%s]\n", pancake);
}

int main(){
    int ca;
    int N;
    char pancake[121];
    scanf("%d", &ca);
    for(int t=0;t<ca;t++){
        scanf("%s",pancake);
        printf("Case #%d: ", t + 1);
        
        int ans = 0;
        for(int end = strlen(pancake) - 1; end>=0;end--){
            if(pancake[end] == '+')continue;
            int beginPositive = 0;
            for(;beginPositive<end;beginPositive++){
                if(pancake[beginPositive] == '-')break;
            }
            //printf("[%s] beginPositive = %d end = %d\n", pancake, beginPositive, end);
            if(! (beginPositive == 0 || beginPositive == end + 1)){
                reverse(pancake, beginPositive);
                ans++;
            }
            reverse(pancake, end + 1);
            ans++;
        }
        printf("%d\n", ans);

    }
    return 0;
}
