#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
#define MAXN 1010
char s[MAXN];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int _,n;
    for(int kcas = scanf("%d",&_);kcas <= _;kcas++)
    {
        scanf("%d%s",&n,s);
        int cnt = 0,ans = 0;
        for(int i = 0;i <= n;i++)
        {
            if(i > cnt)
            {
                ans += i - cnt;
                cnt = i;
            }
            cnt += s[i] - '0';
            //cout << i << " i cnt " << endl;
            //cout << ans << " ans " << endl;
        }
        printf("Case #%d: %d\n",kcas,ans);
    }
}
