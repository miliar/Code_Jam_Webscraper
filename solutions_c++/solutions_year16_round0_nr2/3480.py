#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<cstring>

using namespace std;

char sign(bool v){if(v)return '+';return '-';}
bool get(char ch){if(ch=='+')return true;return false;}


int check(string pancakes,bool choice){
    int lastIndex=-1;

    for(int i=0;i<pancakes.length();i++){

        if(pancakes[i]==sign(!choice)){
            lastIndex=i;
        }
    }

    if(lastIndex==-1)return 0;

    bool sgn=get(pancakes[0]);
    int count=1;

    for(int i=0;i<=lastIndex;i++){
        if(get(pancakes[i])!=sgn){
            count++;
            sgn=!sgn;
        }
    }
    return count;
}

int main(){

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w+",stdout);
    int n;
    string pancakes;

    while(scanf("%d",&n)==1){

        for(int i=1;i<=n;i++){
            cin>>pancakes;
            printf("Case #%d: %d\n",i,check(pancakes,true));
        }
    }


    return 0;
}
