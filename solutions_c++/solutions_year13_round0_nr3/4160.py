#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

const int maxn = 10000000;

#define LL long long

LL f[maxn];
int a[100];
int cnt;

bool judge(LL x)
{
    int n = 0;
    while (x > 0)
    {
        a[++n] = x%10;
        x/=10;
    }

    int l = 1 , r = n;
    bool flag = true;
    while (l < r)
    {
        if (a[l] != a[r])
        {
            flag = false;
            break;
        }
        l++; r--;
    }
    return flag;
}

void init()
{
    cnt = 0;
    for (int i=1;i<maxn;i++)
    {
        if (judge(i) && judge((LL)i*i))
        {
            //cout<<(LL)i*i<<endl;
            f[++cnt] = (LL)i*i;
        }
    }
    //cout<<cnt<<endl;
}

int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    init();
    int t,c=0;
    scanf("%d",&t);
    while (t--)
    {
        LL l,r;
        cin>>l>>r;
        int ans = 0;
        for (int i=1;i<=cnt;i++) if (f[i] >= l && f[i] <= r) ans++;
        printf("Case #%d: ",++c);
        cout<<ans<<endl;
    }
    return 0;
}
