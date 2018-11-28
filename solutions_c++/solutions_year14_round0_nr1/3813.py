#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int t, c=1, x, y, a[4][4], b[4][4], i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d", &a[i][j]);
        }
        scanf("%d", &y);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d", &b[i][j]);
        }
        int flag=0, p;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[x-1][i]==b[y-1][j]) {
                    flag++;
                    p=i;
                }
                if(flag>1)
                    break;
            }
        }
        if(flag==0)
            printf("Case #%d: Volunteer cheated!\n", c);
        else if(flag>1)
            printf("Case #%d: Bad magician!\n", c);
        else if(flag==1)
            printf("Case #%d: %d\n", c, a[x-1][p]);
        c++;
    }
    return 0;
}
