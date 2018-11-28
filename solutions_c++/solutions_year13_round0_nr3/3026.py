#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
long long int p=0,N=0;
int main () {
    scanf("%d",&N);
    for(p=1;p<=N;p++){
        long long int A=0,B=0,cnt=0;
        long long i=0;
        scanf("%lld%lld",&A,&B);
        A-=1;
        A=sqrt(A);
        A+=1;
        B=sqrt(B);
        //printf("%lld %lld\n",A,B);
        for(i=A;i<=B;i++){
            //printf("%lld\n",i);
            bool FUCK=0;
            long long tmp=i,places=0,stack[200]={0},j=0;
            tmp=i;
            //printf("FIRST : TMP : %lld\n",tmp);
            while(tmp>0){
                places++;
                stack[places]=tmp%10;
                tmp/=10;
            }
            for(j=1;j<=places/2;j++){
                if(stack[j]!=stack[places+1-j]){
                    //printf("%lld\n",j);
                    FUCK=1;
                    break;
                }
            }
            if(FUCK==0){
                stack[200]={0};
                tmp=i*i;
                //printf("2nd part TMP : %lld \n",tmp);
                places=0;
                //printf("TMP : %lld\n",tmp);
                while(tmp>0){
                    places++;
                    stack[places]=tmp%10;
                    tmp/=10;
                }
                for(j=1;j<=places/2;j++){
                    if(stack[j]!=stack[places+1-j]){
                        FUCK=1;
                        break;
                    }
                }
            }
            if(FUCK==0){cnt++;}
            //printf("%lld %lld\n",i,places);
        }
        printf("Case #%lld: %lld\n",p,cnt);
        //printf("%lld %lld\n",A,B);
    }
    return 0;
}
