#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define fi first
#define se second
#define mem(a,b) memset((a),(b),sizeof(a))

string s;
int K;

int main()
{
    freopen("/Users/xuehao/Documents/s1/in", "r", stdin);
    freopen("/Users/xuehao/Documents/s1/out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas)
    {
        printf("Case #%d: ",cas);
        cin>>s>>K;
        int ans=0;
        int len=s.length();
        for(int i=0;i<=len-K;++i)
            if(s[i]=='-')
            {
                for(int j=0;j<K;++j)
                    s[i+j]=s[i+j]=='+'?'-':'+';
                ++ans;
            }
        for(int i=0;i<len;++i)
            if(s[i]=='-')
            {
                ans=-1;
                break;
            }
        if(ans==-1)
            puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    
    return 0;
}
