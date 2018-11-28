#include <bits/stdc++.h>
using namespace std;

const int N = 1000 + 10;

int ans[N];
int f[N];
int x;
int p1,p2;
int cnt;
bool v[N];

void init()
{
    cin>>x;
}

void work()
{
    if(x == 0)
    {
        printf("INSOMNIA\n");
        return;
    }
    memset(ans , 0 , sizeof(ans));
    memset(v , 0, sizeof(v));
    p1 = p2 = cnt = 0;
    while(x)
    {
        p1++;
        f[p1] = x % 10;
        x /= 10;
    }
    p2 = p1;

    while(cnt <= 9)
    {
        for(int i = 1;i <= p1;i++)
        {
            ans[i] += f[i];
            if(ans[i] >= 10)
            {
                ans[i] -= 10;
                ans[i + 1]++;
            }
        }

        if(ans[p2 + 1] > 0) p2++;

        for(int i = 1;i <= p2;i++)
        if(!v[ans[i]])
        {
            v[ans[i]] = true;
            cnt++;
        }
    }

    for(int i = p2;i >= 1;i--)
      printf("%d",ans[i]);
    printf("\n");
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

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
