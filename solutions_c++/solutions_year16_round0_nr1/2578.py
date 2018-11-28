#include <iostream>
#include<stdio.h>
using namespace std;
long long x, nr, j, ex[15], t;

void marcare(long long a){
    while (a){
        nr-=(1-ex[a%10]);
        ex[a%10]=1;
        a/=10;
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        scanf("%d",&x);
        for (int j=0;j<=9;j++)
            ex[j]=0;
        if (x){
            j=1;    nr=10;
            while (nr){
                marcare(j*x);
                j++;
            }
            printf("Case #%ld: %ld\n",i,(j-1)*x);
        }else
            printf("Case #%ld: INSOMNIA\n",i);
    }
    return 0;
}
