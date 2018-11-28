#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;

char s[32];

void check_prime(int n,int i){
    n = n/2 -2;    
    memset(s,'0',sizeof(s));
    s[n] = '\0';
    while(i){
        s[n-1] = '0' + (i % 2);
        i = i /2;
        n--;
    }
    printf("1%s11%s1",s,s);
    for(int b = 2 ; b <= 10 ; b++){
        int res = pow(b,8) + 1;
        printf(" %d",res);
    }
    printf("\n");
}

int main(){
    int N = 16,J=50;
    printf("Case #1:\n");
    for(int i = 0 ; i < 50; i++){
        check_prime(N,i);
    }
    return 0;
}