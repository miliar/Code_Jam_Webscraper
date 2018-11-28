#include<cstdio>
char matrix[4][4][4]={'G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G',
                    'R','G','R','G','G','G','G','G','R','G','R','G','G','G','G','G',
                    'R','R','R','R','R','R','G','R','R','G','G','G','R','R','G','R',
                    'R','R','R','R','R','R','R','R','R','R','R','G','R','R','G','G'};
//x, r, c
int main()
{
    int x, r, c, t;
    freopen("D-small-attempt3.in","r",stdin);
    freopen("./d.out","w",stdout);
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        switch (matrix[x-1][r-1][c-1])
        {
            case 'G':printf("Case #%d: GABRIEL\n",i);break;
            case 'R':printf("Case #%d: RICHARD\n",i);break;
        }
    }
    return 0;
}
