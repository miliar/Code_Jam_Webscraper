#include<stdio.h>

int t,n,am,baga;
int v[1005];

int main ()
{
    int i,j;
    char car;

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d",&t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d ",&n);
        for(j = 0; j <= n; j++)
        {
            scanf("%c",&car);
            v[j] = car - '0';
        }
        am = 0;baga = 0;
        for(j = 0; j <= n; j++)
            if(am >= j)
                am += v[j];
            else
            {
                baga += j - am;
                am = j + v[j];
            }
        printf("Case #%d: %d\n",i,baga);
    }

    return 0;
}
