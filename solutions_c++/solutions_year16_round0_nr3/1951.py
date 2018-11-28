#include <cstdio>
int N,J,now;
int output[50];
void solve()
{
    if(J==0)return;
    if(now*2+2==N)
    {
        J--;
        printf("1");
        for(int i=0;i<now;i++)
        {
            printf("%d%d",output[i],output[i]);
        }
        printf("1 3 4 5 6 7 8 9 10 11\n");
        return;
    }
    output[now]=0;
    now++;
    solve();
    now--;
    output[now]=1;
    now++;
    solve();
    now--;
    return;
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        now=0;
        printf("Case #%d:\n",i);
        scanf("%d%d",&N,&J);
        solve();
    }
}
