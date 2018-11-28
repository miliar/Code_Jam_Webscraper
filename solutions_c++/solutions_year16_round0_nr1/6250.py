#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int tst;
    scanf("%lld",&tst);
    for(long long int r=1;r<=tst;r++)
    {

    long long int a[10]={0};
    long long int i,n,p;

    scanf("%lld",&n);
    if(n==0)
        printf("Case #%lld: INSOMNIA\n",r);
    else{
    for( i=1;i>0;i++)
    {
        p=n*i;
    while(p>0)
    {
        long long int c=p%10;
        a[c]=1;
        p=p/10;
    }
    long long int co=0;
    for(long long int n=0;n<=9;n++)
    {
        if(a[n]==1)co++;
    }
    if(co==10)break;
    }
    printf("Case #%lld: %lld\n",r,n*i);
    }
    }
    return 0;
}
