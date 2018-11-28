#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
const int MAXN = 1e6;
int fg[10];
int res,cnt;

void check_num(int n){
    int c;
    while(n){
        c = n % 10;
        if(!fg[c]){
            fg[c] = 1;
            cnt++;
        }
        n = n / 10;
    }
}

int main(){
    int N,T;
    scanf("%d",&T);
    for(int i = 1 ; i <= T ; i++){
        scanf("%d",&N);
        res = -1;
        cnt = 0;
        memset(fg,0,sizeof(fg));
        int n = N;
        while(n <= MAXN){
            if(n == 0) break;
            check_num(n);
            if(cnt == 10){
                res = n;
                break;
            }
            n += N;
        }
        if(res == -1)
            printf("Case #%d: INSOMNIA\n",i);
        else
            printf("Case #%d: %d\n",i,res);
    }
    return 0;
}