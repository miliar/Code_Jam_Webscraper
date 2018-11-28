#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int got;
bool seen[10];

void find(int n)
{
    int tmp;
    while (n)
    {
        tmp=n%10;
        n=n/10;
        if (!seen[tmp])
        {
            seen[tmp]=true;
            got++;
        }
    }
}

int main()
{
    int n,t,ans,T;
    long long curr;
    scanf("%d",&T);
    for (t=0;t<T;t++)
    {
        printf("Case #%d: ",t+1);
        scanf("%d",&n);
        if (n)
        {
            ans=1; got=0;
            memset(seen,0,sizeof(seen));
            while (got!=10)
            {
                curr=n*ans;
                find(curr);
                ans++;
            }
            printf("%lld\n",curr);
        }
        else printf("INSOMNIA\n");
    }
}
