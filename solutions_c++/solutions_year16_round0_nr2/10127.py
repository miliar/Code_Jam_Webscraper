#include<stdio.h>
#include<string.h>

char pancakes[100];

void reverse(int end){
    char aux;
    /*for(int i = 0; i <= end; i++){
        aux = pancakes[i];
        pancakes[i] = pancakes[end-i];
        pancakes[end-i] = aux;
    }*/
    if(pancakes[0] == '-') aux = '+';
    else aux = '-';
    for(int i = 0; i <= end; i++){
        pancakes[i] = aux;
    }
}

int editDistance(int n){
    int i = 0;
    char c = 'v';
    int cnt = 0;
    while(i < n){
        if(c == 'v'){
            c = pancakes[i];
            i++;
        }else if(c != pancakes[i]){
            //reverse(i-1);
            cnt++;
            c = 'v';
        }else i++;
    }
    if(pancakes[n-1] == '-') cnt++;
    return cnt;
}

int main(void){
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++){
        scanf("%s",pancakes);
        printf("Case #%d: %d\n",i, editDistance(strlen(pancakes)));
    }
    return 0;
}
