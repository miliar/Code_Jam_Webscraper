//
//  main.cpp
//  Round 1C 2014. Problem A. Part Elf
//
//  Created by kimtaeyang on 2014. 5. 11..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <string.h>

long gcd(long  A, long  B){
    if(!B) return A;
    return gcd(B,A%B);
}
struct INTEGER{
    long long a,b;
    void G(){
        long long c=gcd(a,b);
        a/=c; b/=c;
    }
    void input(){
        char s[100];
        int st=0;
        scanf("%s",s);
        b=1;
        for(int i=st;i<strlen(s);i++){
            if(s[i]=='/'){
                b=0;
                for(++i;s[i];i++){
                    b = b*10 + s[i]-'0';
                }
            }
            else if(s[i]=='.'){
                for(++i;s[i];i++){
                    b*=10;
                    a = a*10 + s[i]-'0';
                }
            }
            else {
                a = a*10 + s[i]-'0';
            }
        }
        G();
        if(st) a=-a;
    }
};

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T,I;
    
    scanf("%d",&T);
    
    INTEGER k;
    int i;
    long long b;
    
    for(I=1;I<=T;I++){
        k.a=k.b=0;
        k.input();
        b=k.b;
        for(b=k.b;!(b&1);b>>=1);
        if(b!=1) printf("Case #%d: impossible\n",I);
        else {
            for(i=0;;i++){
                if(k.a==1 && k.b==1) break;
                //if(k.a*2>k.b) k.b/=2, k.a=k.a-k.b;
                if(k.a*2>k.b){i++; break;}
                else k.b/=2;
            }
            printf("Case #%d: %d\n",I,i);
        }
    }
    
}