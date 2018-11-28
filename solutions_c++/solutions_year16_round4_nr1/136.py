#pragma warning(disable:4996)

#include <stdio.h>
#include <algorithm>
using std::swap;

char ans[8192];
char tmp[8192];

void sort(char *x, int n)
{
    if (!n)
        return;

    sort(x, n-1);
    sort(x + (1<<(n-1)), n-1);

    for (int i=0; i<(1<<(n-1)); i++)
    {
        if (x[i] < x[i+(1<<(n-1))])
            return;
        else if (x[i] > x[i+(1<<(n-1))])
        {
            for (int j=0; j<(1<<(n-1)); j++)
                swap(x[j], x[j+(1<<(n-1))]);
            return;
        }
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while (t--)
    {
        int n, a[3];
        scanf("%d", &n);
        for (int i=0; i<3; i++) scanf("%d", &a[i]);

        int b[3];
        b[0]=b[1]=1;
        b[2]=0;
        ans[0] = 'R';
        ans[1] = 'P';
        int c[3];
        for (int i=1; i<n; i++)
        {
            c[0]=c[1]=c[2]=0;
            for (int j=0; j<3; j++)
            {
                c[j] += b[j];
                c[(j+1)%3] += b[j];
            }

            for (int j=0; j<(1<<(i)); j++)
            {
                tmp[j*2] = ans[j];
                tmp[j*2+1] = ans[j]=='R' ? 'P' : ans[j] == 'P' ? 'S' : 'R';
            }
            for (int j=0; j<(1<<(i+1)); j++)
                ans[j] = tmp[j];

            b[0]=c[0];
            b[1]=c[1];
            b[2]=c[2];
        }

        int x=-1;
        for (int k=0; k<3; k++)
        {
            bool fail=false;
            for (int i=0; i<3; i++)
                if (a[i] != b[(k+i)%3])
                    fail = true;

            if (!fail)
                x=k;
        }

        printf("Case #%d: ", ++tt);
        if (x==-1) printf("IMPOSSIBLE\n");
        else
        {
            for (int i=0; i<x; i++)
            {
                for (int j=0; j<(1<<n); j++)
                {
                    if (ans[j]=='R') ans[j] = 'S';
                    else if (ans[j]=='P') ans[j] = 'R';
                    else if (ans[j]=='S') ans[j] = 'P';
                }
            }
            ans[(1<<n)] = 0;
            sort(ans, n);
            printf("%s\n", ans);
        }
    }

    return 0;
}
