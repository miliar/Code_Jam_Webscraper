#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main(){
    int K,C,S,T;
    scanf("%d",&T);
    for(int i = 1 ; i <= T ; i++){
        scanf("%d %d %d",&K,&C,&S);
        printf("Case #%d:",i);
        for(int j = 1 ; j <= K ; j++) printf(" %d",j);
        printf("\n");
    }
}