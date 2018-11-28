
#include <iostream>
#include<stdio.h>
int t;
long long k, c, s, x, put, u=1, j, poz, pr;
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        scanf("%d %d %d\n",&k,&c,&s);
        printf("Case #%d:",i);
        if (s>=k){
            for (pr=1;pr<=k;pr++){
                poz=pr;
                for (int i=2;i<=c;i++){
                    poz=k*(poz-u)+u;

                }
                printf(" %lld",poz);
            }
            printf("\n");
        }else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
