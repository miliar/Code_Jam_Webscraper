#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
using namespace std;
int ans[20];
int cas;
int a;
void fix(int p)
{
    while(p)
    {
        ans[p % 10] = 1;
        p /= 10;
    }
}
bool check()
{
    for (int i = 0 ; i < 10 ; i ++)
        if (ans[i] == 0) return false;
    return true;
}
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&cas);
    for (int _ = 1 ; _ <= cas ; _++)
    {
        printf("Case #%d: ",_);
        int flag = 0;
        memset(ans,0,sizeof(ans));
        scanf("%d",&a);
        for (int i = 1 ; i < 1000 ; i ++)
        {
            int now = a * i;
            fix(now);
            if (check())
            {
                flag = 1;
                printf("%d\n",now);
                break;
            }
        }
        if (!flag)
        printf("INSOMNIA\n");
    }
    fclose(stdin);
    fclose(stdout);
}
