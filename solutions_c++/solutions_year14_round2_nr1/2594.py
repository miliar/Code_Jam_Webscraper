#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main(void)
{
    int t, n, i, j, k, l, tc=0, tmp, res, data[105][105];
    char chr[105], memo[105][105];
    bool valid;
    for (scanf("%d", &t);t--;)
    {
        scanf("%d", &n);
        for (i=0;i<n;i++)
        {
            scanf("%s", chr);
            k=0;
            l=strlen(chr);
            data[i][k]=1;
            memo[i][k]=chr[0];
            for (j=1;j<l;j++)
                if (chr[j]==memo[i][k])
                    data[i][k]++;
                else
                {
                    k++;
                    data[i][k]=1;
                    memo[i][k]=chr[j];
                }
            data[n][i]=k;
        }
        valid=1;
        for (i=1;i<n && valid;i++)
        {
            valid&=(data[n][i]==data[n][i-1]);
            for (j=0;j<=data[n][i] && valid;j++)
                valid&=(memo[i][j]==memo[i-1][j]);
        }
        printf("Case #%d: ", ++tc);
        if (!valid)
            printf("Fegla Won\n");
        else
        {
            res=0;
            for (j=0;j<=data[n][0];j++)
            {
                k=0;
                for (i=0;i<n;i++)
                    k+=data[i][j];
                l=k/n;
                tmp=0;
                for (i=0;i<n;i++)
                    tmp+=abs(data[i][j]-l);
                if (k%n)
                {
                    l++;
                    k=0;
                    for (i=0;i<n;i++)
                        k+=abs(data[i][j]-l);
                    tmp=min(tmp, k);
                }
                res+=tmp;
            }
            printf("%d\n", res);
        }
    }
    return 0;
}
