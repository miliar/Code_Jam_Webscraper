#include <iostream>
#include<stdio.h>
#define N 100000
using namespace std;

long long nrfinal(int x)
{
    int a[10];
    for(int i=0;i<=9;i++)
        a[i]=0;
    unsigned long long nr=0,aux;
    int j=0;
    while(nr<=9)
    {
        j++;
        aux=j*x;
        while(aux!=0)
        {
            if(a[aux%10]==0)
                nr++;
            a[aux%10]=1;
            aux/=10;
        }


    }
    return j*x;
}
int t;
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int maxi=0;
    int indice=0;
    int x;
    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
        scanf("%d",&x);
        if(x==0)
            printf("Case #%d: INSOMNIA\n",i);
        else
        printf("Case #%d: %lld\n",i,nrfinal(x));
//        if(nrfinal(i)>=maxi)
//        {
//            maxi=nrfinal(i);
//            indice=i;
//        }
    }
       // printf("%d %d",maxi,indice);
        return 0;
}
