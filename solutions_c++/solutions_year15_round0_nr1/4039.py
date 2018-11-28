#include <cstdio>
int T,smax;
char a[1100];
int i,q,ans,cn;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for (q=1;q<=T;q++)
    {
        scanf("%d",&smax);
        scanf(" %s",a);

        cn = 0; ans = 0;
        for (i=0;i<=smax;i++)
            if (cn<i)
            {
                ans += (i-cn);
                cn = cn + (i- cn)+a[i]-'0';
            }
            else
                cn = cn + a[i]-'0';

        printf("Case #%d: %d\n",q,ans);
    }



    return 0;
}
