#include <cstdio>

using namespace std;

int main(void)
{
    int t, r, c, m, n, i, j, tc=0;
    char chr[55][55];
    bool flag, valid;
    for (scanf("%d", &t);t--;)
    {
        flag=0;
        valid=1;
        scanf("%d%d%d", &r, &c, &m);
        n=r*c-m;
        if (r>c)
        {
            r^=c^=r^=c;
            flag=1;
        }
        if (!m)
        {
            for (i=0;i<r;i++)
                for (j=0;j<c;j++)
                    chr[i][j]='.';
        }
        else if (n==1)
        {
            for (i=0;i<r;i++)
                for (j=0;j<c;j++)
                    chr[i][j]='*';
        }
        else if (r==1)
        {
            for (j=0;j<c;j++)
                chr[0][j]=((j<m) ? ('*') : ('.'));
        }
        else if (!(n&1) && r>=2 && n>=4)
        {
            for (i=0;i<r;i++)
                for (j=0;j<c;j++)
                    chr[i][j]='.';
            for (i=0;m && i<r-2;i++)
                for (j=0;m && j<c-2;j++,m--)
                    chr[i][j]='*';
            for (i=0;m && i<r-2;i++,m-=2)
            {
                chr[i][c-2]='*';
                chr[i][c-1]='*';
            }
            for (j=0;m && j<c-2;j++,m-=2)
            {
                chr[r-2][j]='*';
                chr[r-1][j]='*';
            }
        }
        else if ((n&1) && r>=3 && n>=9)
        {
            for (i=0;i<r;i++)
                for (j=0;j<c;j++)
                    chr[i][j]='.';
            for (i=0;m && i<r-3;i++)
                for (j=0;m && j<c-2;j++,m--)
                    chr[i][j]='*';
            for (j=0;m && j<c-3;j++,m--)
                chr[r-3][j]='*';
            for (i=0;m && i<r-3;i++,m-=2)
            {
                chr[i][c-2]='*';
                chr[i][c-1]='*';
            }
            for (j=0;m && j<c-3;j++,m-=2)
            {
                chr[r-2][j]='*';
                chr[r-1][j]='*';
            }
        }
        else
            valid=0;
        printf("Case #%d:\n", ++tc);
        if (valid)
        {
            chr[r-1][c-1]='c';
            if (flag)
                r^=c^=r^=c;
            for (i=0;i<r;i++)
            {
                for (j=0;j<c;j++)
                    printf("%c", ((flag) ? (chr[j][i]) : (chr[i][j])));
                printf("\n");
            }
        }
        else
            printf("Impossible\n");
    }
    return 0;
}
