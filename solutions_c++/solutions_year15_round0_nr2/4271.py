#include<iostream>
#include<stdio.h>
using namespace std;
int ar[1001];
long long int func(long long int x, int D)
{
    long long int sum=0;
    for(int i=0;i<D;i++)
    {
        sum+=(ar[i]-1)/x;
    }
    return sum;
}
int main()
{
    //cout<<min(1000000000000, 1000000000001);
    freopen("paninfile.in","r",stdin);
    freopen("panoutfile.txt","w",stdout);
    int t, D, maxele;
    long long int ans;
    scanf("%d", &t);
    for(int tcase=1;tcase<=t;tcase++)
    {
        scanf("%d%d", &D, &ar[0]);
        maxele=ar[0];
        for(int i=1;i<D;i++)
        {
            scanf("%d", &ar[i]);
            if(maxele<ar[i])
                maxele=ar[i];
        }
        ans=maxele;
        long long int cont=2;
        while(cont<ans)
        {
            ans=min(ans, func(cont, D)+cont);
            cont++;
        }
        printf("Case #%d: %lld", tcase, ans);
        printf("\n");
    }
}
