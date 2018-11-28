#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int T,n;
char str[1010];

int main()
{
    char inpath[100] = "C:\\Users\\Bin\\Downloads\\A-large.in";
    char outpath[100] = "C:\\Users\\Bin\\Downloads\\A-large.out";
    freopen(inpath,"r",stdin);
    freopen(outpath,"w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d %s",&n, str);

        int cur = 0;
        int ans = 0;

        for(int i=0;i<=n;i++)
        {
            if(i>cur)
            {
                ans += (i-cur);
                cur = i;
            }
            cur += str[i]-'0';
        }

        printf("Case #%d: %d\n", t,ans);
    }
}
