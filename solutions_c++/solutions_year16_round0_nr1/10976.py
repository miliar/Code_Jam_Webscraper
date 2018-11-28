#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool visited[10];

int main ()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, x, i, y, flag=0, j, k, l, cs=0, ans;
    scanf("%d", &t);
    while (t--)
    {
        cs++;
        ans=0;
        for (i=0; i<10; i++) visited[i]=false;
        scanf("%d", &n);
        if (n==0)
        {
            printf("Case #%d: INSOMNIA\n", cs);
            continue;
        }
        flag=0;
        i=1;
        while (!flag)
        {
            x = n*i;
            while (x!=0)
            {
                y=x%10;
                visited[y]=true;
                x/=10;
            }
            for (j=0; j<10; j++)
            {
                if (visited[j]==false)
                {
                    flag=0;
                    break;
                }
            }
            if (j==10)
            {
                flag=1;
                ans=n*i;
            }
            i++;
        }
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}
