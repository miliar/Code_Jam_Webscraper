#include<iostream>
#include<stdio.h>
#include <math.h>
using namespace std;
int digit[20];
int digit2[20];
int palSS(int x){
    int id = 0;
    while( x  ){
        digit2 [id++]=x%10;
        x /=10;
    }
    if(!id)return 0;

    bool t =true;
    for( int k = 0; k < id; k++){
        if(digit2 [k]!= digit2[id-k-1]) t = false;
    }
    if(t)return 1;
    return 0;
}
int palS(int x){
    //if( x < 10) return 1;
    int X= x;
    int id = 0;
    while( x  ){
        digit [id++]=x%10;
        x /=10;
    }
    bool t =true;
    for( int k = 0; k < id; k++){
        if(digit [k]!= digit[id-k-1]) t = false;
    }
    if(t)return palSS (X*X);
    return 0;
}
int main(){
    int t,a, b;
    scanf("%d",&t);
    for(int i =0; i <t; i++){
        scanf("%d %d",&a, &b);
        int wyn=0;
        for(int j=ceil(sqrtf(a)); j <=floor(sqrt(b)); j++){
             wyn+=palS(j);


        }
        printf("Case #%d: %d\n",i+1, wyn);
    }
    return 0;
}
