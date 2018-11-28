#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.in.txt","w",stdout);
    char bg[51][51];
    int T,TT;
    int sw,r,c,m,n,i,j,impossible;
    scanf("%d",&TT);
    for (T=1;T<=TT;T++)
    {
        sw = 0;
        impossible = 0;
        printf("Case #%d:\n",T);
        scanf("%d %d %d",&r,&c,&m);
        n = r*c-m;
        if (r>c)
        {
            swap (r,c);
            sw = 1;
        }
        for (i=1;i<=r;i++)
            for (j=1;j<=c;j++)
                bg[i][j] = '*';
        if (r==1)
        {
            for (i=1;i<=n;i++)
                bg[1][i] = '.';
            bg[1][1] = 'c';
        }
        else if (r==2)
        {
            if (n>3 and n%2==0)
            {
                for (i=1;i<=2;i++)
                    for (j=1;j<=n/2;j++)
                        bg[i][j] = '.';
            }
            else if (n>1)
                impossible = 1;
            bg[1][1] = 'c';
        }
        else
        {
            if (n==1);
            else if (n==2 or n==3 or n==5 or n==7)
                impossible = 1;
            else
            {
                for (i=1;i<=c;i++)
                {
                    if (n>=2)
                    {
                        bg[1][i] = '.';
                        bg[2][i] = '.';
                        n -= 2;
                    }
                    else if (n==1)
                    {
                        bg[1][i-1] = '*';
                        bg[2][i-1] = '*';
                        bg[3][1] = '.';
                        bg[3][2] = '.';
                        bg[3][3] = '.';
                        n--;
                        break;
                    }
                    else
                        break;
                }
                if (n>0)
                {
                    if (n==1)
                    {
                        bg[1][c] = '*';
                        bg[2][c] = '*';
                        bg[3][1] = '.';
                        bg[3][2] = '.';
                        bg[3][3] = '.';
                        n--;
                    }
                    else
                    {
                        for (i=1;i<=c;i++)
                        {
                            if (n>=1)
                            {
                                bg[3][i] = '.';
                                n--;
                            }
                            else
                                break;
                        }
                    }
                }
                i = 3;
                while (n>0)
                {
                    i++;
                    if (n==1)
                    {
                        bg[i][1] = '.';
                        bg[i][2] = '.';
                        bg[i-1][c] = '*';
                        n--;
                    }
                    else
                    {
                        for (j=1;j<=c;j++)
                        {
                            if (n>=1)
                            {
                                bg[i][j] = '.';
                                n--;
                            }
                            else
                                break;
                        }
                    }
                }
            }
            bg[1][1] = 'c';
        }
        if (impossible)
            printf("Impossible\n");
        else
        {
            if (sw)
            {
                for (i=1;i<=c;i++)
                {
                    for (j=1;j<=r;j++)
                        printf("%c",bg[j][i]);
                    printf("\n");
                }
                printf("\n");
            }
            else
            {
                for (i=1;i<=r;i++)
                {
                    for (j=1;j<=c;j++)
                        printf("%c",bg[i][j]);
                    printf("\n");
                }
                printf("\n");
            }
        }
    }
}
