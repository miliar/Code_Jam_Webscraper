#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

int t;
int n,ansl,ansr;
char ansstr[2002],a[1001];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        scanf(" %s",a);
        n=strlen(a);
        ansl=ansr=n;
        ansstr[ansl]=a[0];
        for(int i=1;i<n;i++)
        {
            int k=ansl;
            while(ansstr[k]==a[i] && k<ansr)
                ++k;
            if(a[i]<ansstr[k])
                ansstr[++ansr]=a[i];
            else
                ansstr[--ansl]=a[i];
        }
        printf("Case #%d: ",cas);
        for(int i=ansl;i<=ansr;++i)
            printf("%c",ansstr[i]);
        printf("\n");
    }
    return 0;
}
