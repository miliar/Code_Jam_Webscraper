#include <bits/stdc++.h>
using namespace std;

const int N = 1000 + 10;

char f[N],x = '+' + '-';
int n,ans = 0;

void init()
{
    scanf("%s",f + 1);
    n = strlen(f + 1);
    ans = 0;
}

void work()
{
    for(int i = n;i >= 1;i--)
    {
        if(f[i] == '-')
        {
            ans++;
            for(int j = 1;j <= i;j++)
              f[j] = x - f[j];
        }
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    cin>>T;
    for(int i = 1;i <= T;i++)
    {
        init();
        printf("Case #%d: ",i);
        work();
    }
    return 0;
}
