#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int i,k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        assert(s==k);
        printf("Case #%d: ",cs);
        cs++;
        for(i=1;i<=k;i++)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}
