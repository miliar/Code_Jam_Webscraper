#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#define ll long long
using namespace std;
int main()
{
    int n, i, j, x, y, t, m, k;
    int a[10][10], b[10][10];
    freopen("5.txt","r",stdin);
    freopen("6.txt","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        y=0;
        scanf("%d",&n);
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&m);
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                if(b[m-1][j]==a[n-1][i])
                {
                    x=a[n-1][i];
                    y++;
                    break;
                }
            }
        }
        printf("Case #%d: ", k);
            if(y==1)
                printf("%d\n",x);
            else if(y>1)
                printf("Bad magician!\n");
            else
                printf("Volunteer cheated!\n");
    }
    return 0;
}
