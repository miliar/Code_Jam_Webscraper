#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<cstring>

using namespace std;

int array[50];


int bin=1;

void nextPerm(int N){
    array[0]=1;
    array[N-1]=1;

    int temp=bin;
    int mask=1;
    for(int i=1;i<=N-2;i++){
        array[N-1-i]=temp&mask;
        temp=temp>>1;
    }
    bin++;
}

long long getNumber(int N,int base){
    long long sum=0;
    for(int i=0;i<N;i++){
        sum=sum*base+array[i];
    }
    return sum;
}

long long isPrime(long long n){
    if(n<=1)return -1;
    for(long long i=2;i*i<n;i++){
        if(n%i==0)return i;
    }
    return -1;
}

long long numbers[11];

void printN(int N){
    for(int j=0;j<N;j++){
            printf("%d",array[j]);
    }
}

void check(int N,int J){

    /*for(int i=0;i<10;i++){
        for(int j=0;j<N;j++){
            cout<<array[j]<<" ";
        }
        cout<<"\t"<<getNumber(N,2)<<endl;
        nextPerm(N);
    }*/

    int count=0;
    bool flag=false;

    while(count<J){

        flag=true;
        for(int i=2;i<=10;i++){
            numbers[i-2]=isPrime(getNumber(N,i));
            if(numbers[i-2]==-1){
                    flag=false;
                    break;
            }
        }
        if(flag){
            printN(N);
            for(int i=0;i<=8;i++){
                printf(" %lld",numbers[i]);
            }
            printf("\n");
            count++;
        }

        nextPerm(N);
    }


}



int main(){

    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w+",stdout);
    int n;
    int N,J;

    while(scanf("%d",&n)==1){

        for(int i=1;i<=n;i++){
            scanf("%d%d",&N,&J);
            array[0]=1;
            array[N-1]=1;
            bin=1;
            printf("Case #%d: \n",i);
            check(N,J);
            printf("\n");
        }
    }


    return 0;
}
