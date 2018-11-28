#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ts,k,c,s,i;

    scanf("%d",&ts);

    for(t=1;t<=ts;t++)
    {
        scanf("%d%d%d",&k,&c,&s);

        printf("Case #%d:",t);

        for(i=1;i<=s;i++)
            printf(" %d",i);
        printf("\n");
    }
}
