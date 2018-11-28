#include <iostream>
#include <cstdio>
using namespace std;
#define MAX 1000000

int check(int dig[],int n)
{
    for(int i=0;i<n;i++) {
        if(dig[i]!=1) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int t,T,i,flag,j,dig[10];
    long long int n,ncopy,norig;
    cin>>T;
    for(t=1;t<=T;t++) {
        cin>>norig;
        n=0;
        for(i=0;i<10;i++) dig[i]=0;
        flag=0;
        for(i=1;i<=MAX;i++) {
            n=norig*i;
            ncopy=n;
            while(n>0) {
                dig[n%10]=1;
                n=n/10;
            }
            n=ncopy;
            if(check(dig,10)) {
                flag=1;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(flag) {
            printf("%lld\n",n);
        }
        else {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
