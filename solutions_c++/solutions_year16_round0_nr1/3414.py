#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

bool array[11];

bool isAll(){
    for(int i=0;i<10;i++){
        if(!array[i]){
            return false;
        }
    }

    return true;
}

void update(long long value){

    if(value==0){
            array[0]=true;
            return;
    }
    while(value>0){
        array[value%10]=true;
        value=value/10;
       // cout<<"here"<<endl;


    }
}

long long check(long long value){
    long long n=1;
    long long v;
    while(!isAll()){
        v=value*n;
        update(v);

       // for(int i=0;i<10;i++){
       //     cout<<array[i]<<" ";
       // }
       // cout<<endl;
        //while(1);

        n++;
    }

    return v;
}

int main(){
    int n;
    long long value;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w+",stdout);

    while(scanf("%d",&n)==1){

        for(int i=1;i<=n;i++){
            for(int j=0;j<10;j++){
                array[j]=false;
            }
            scanf("%lld",&value);
            if(value==0){
                printf("Case #%d: INSOMNIA\n",i);
            }
            else{
                printf("Case #%d: %lld\n",i,check(value));
            }

        }
    }


    return 0;
}
