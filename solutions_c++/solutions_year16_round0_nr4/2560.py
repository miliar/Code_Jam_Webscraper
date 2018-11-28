#include<iostream>
#include<stdio.h>

long long power(int n, int p){

    long long result = 1;
    int  i =1;
    result = 1;
    for(i=1;i<=p;i++)
        result = result * n;
    return result;
}

int main(){

    int t,i,case_num=1;
    int k,c,s;
    long long jump;
    scanf("%d",&t);
    while(t-->0){
        scanf("%d%d%d",&k,&c,&s);
        jump = power(k,c-1);
        printf("Case #%d: ",case_num++);
        for(i=0;i<s;i++)
            printf("%lld ",jump*i+1);
        printf("\n");
    }
    return 0;
}
