#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("resA.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",ca);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int vis=0,cnt=0;
        while(1)
        {
            int t=++cnt*n;
            while(t)
            {
                vis|=(1<<t%10);
                t/=10;
            }
            if(vis==(1<<10)-1)break;
        }
        printf("%d\n",cnt*n);
    }
    return 0;
}
