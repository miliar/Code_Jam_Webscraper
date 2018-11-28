#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>

using namespace std;
typedef long long ll;

int flag[12];

int ff(ll x);
int check();

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cass=1;
    while(t--)
    {
        memset(flag,0,sizeof(flag));
        int n;
        scanf("%d",&n);
        ff((ll)n);
        ll ans=(ll)(n),bi=1;
        while(1)
        {
            if(check()) break;
            ans=(ll)(n)*bi;
            ff(ans);
            bi++;
            if(bi>100) break;
        }
        if(bi>100)
            printf("Case #%d: INSOMNIA\n",cass++);
        else
            printf("Case #%d: %lld\n",cass++,ans);
    }
    return 0;
}

int check()
{
    for(int i=0;i<10;i++)
    {
        if(flag[i]==0) return 0;
    }
    return 1;
}

int ff(ll x)
{
    while(x)
    {
        flag[x%10]=1;x/=10;
    }
    return 0;
}
