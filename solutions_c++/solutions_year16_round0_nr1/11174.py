#include <bits/stdc++.h>

using namespace std;

bool arr[10];
bool asum;
long TempCounter;
void check(long long val){
    long i;
    while (val>0)
    {
        if (arr[val%10]==0){
            arr[val%10]=1;
            TempCounter++;
        }
        val=val/10;
    }
    if (TempCounter==10)asum=1;
}

int main(){
    long long x;
    long i,j,k, iT; //iterators
    long n, counter, T;
    long temp;

    scanf("%ld", &T);
    for (iT=1; iT<=T; iT++){
        for (i=0; i<=9; i++)arr[i]=0;

        scanf("%ld",&n);
        //n=iT;
        counter=0;
        asum=0;
        TempCounter=0;
        if (n==0){
            x=-1;
            asum=1;
        }

        while (asum==0) {
            counter++;
            x=counter*n;
            check(x);
        }

        if (x==-1){
            printf("Case #%ld: INSOMNIA\n", iT);
        }else{
            printf("Case #%ld: %lld\n", iT, x);
        }
    }


    return 0;
}
