#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


typedef unsigned long long LL;

LL T,N,J;

LL ans[11];
LL pr[11];

bool check(LL x)
{
    LL v,h;
    for(LL i=2;i<=10;i++)
    {
        ans[i]=-1;

        v=0;
        h=1LL;
        for(LL j=0;j<N;j++)
        {
            v += h*(LL)((x>>j)&1);
            h *= i;
        }

        for(LL j=2;j*j<=v;j++)
        {
            if(v%j==0)
            {
                ans[i]=j;
                pr[i]=v;
                break;
            }
        }

        if(ans[i]==-1)return false;
    }

    return true;
}

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>T>>N>>J;

    printf("Case #1:\n");
    int mined=0;

    for (LL i=32769;;i+=2)
    {
        if(check(i))
        {
            for(int j=N-1;j>=0;j--)printf("%d",(i>>j)&1);


            //for (int j=2;j<=10;j++)printf(" %lld",pr[j]);
            for (int j=2;j<=10;j++)printf(" %lld",ans[j]);
            printf("\n");

            mined++;
            if(mined==J)return 0;
        }
    }


}
