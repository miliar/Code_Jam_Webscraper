#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


typedef unsigned long long LL;

LL powr(LL x, LL y)
{
    if(y==0)return 1LL;
    if(y==1)return x;
    LL z = pow(x,y/2);
    z = z*z;
    if(y%2==1) z*=x;
    return z;
}

int main()
{

    LL T,k,c,s;


    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>T;



    for(int i=1;i<=T;i++)
    {
        cin>>k>>c>>s;
        if(s<k)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else
        {
            LL h = 1LL;
            for (LL j=1;j<c;j++)h=h*k;
            printf("Case #%d: ",i);
            for(LL j=0;j<k;j++)printf("%lld ",1LL+h*j);
            printf("\n");
        }
    }

}
