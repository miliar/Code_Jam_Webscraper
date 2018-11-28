#include<iostream>
#include<cstdio>
using namespace std;

int T;
bool vis[10+5];

int Cul(int x)
{
    int cnt=0;
    do
    {
        cnt+=(!vis[x%10]);
        vis[x%10]=true;
        x/=10;
    }while(x);
    return cnt;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        int n, m=0, cnt=0;
        scanf("%d", &n);
        memset(vis, false, sizeof vis);

        printf("Case #%d: ", i);
        for(int j=1; j<=200; j++)
        {
            m+=n;
            cnt+=Cul(m);
            if(cnt==10)
            {
                printf("%d\n", m);
                break;
            }
        }
        if(cnt!=10) printf("INSOMNIA\n");
    }
    return 0;
}
