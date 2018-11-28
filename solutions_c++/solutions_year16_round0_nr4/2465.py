#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    int cur=1;
    scanf("%d",&t);
    while(t--)
    {
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",cur);
        for(int i=0;i<s;i++) printf("%d ",i+1);
        printf("\n");
        cur++;
    }
    return 0;
}
