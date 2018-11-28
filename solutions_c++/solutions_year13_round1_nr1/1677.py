#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<cstdio>
#include <fstream>
#include<cstring>
#include<cmath>
#include <string>
using namespace std;
long long int N=0,i=0;
int main () {
    freopen("Bullseye.in","r",stdin);
    freopen("Bullseye.out","w",stdout);
    scanf("%lld",&N);
    for(i=1;i<=N;i++){
        long long int r=0,t=0,next,answer=0;
        scanf("%lld %lld",&r,&t);
        next=2*r+1;
        while(t-next>=0){
            t-=next;
            answer++;
            r+=2;
            next=2*r+1;
        }
        printf("Case #%lld: %lld\n",i,answer);
    }
    return 0;
}
