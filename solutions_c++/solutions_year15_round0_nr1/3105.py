#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
#define Rep(i,n) for (int i=0;i<(n);i++)
#define For(i,l,r) for (int i=(l);i<=(r);i++)
#define PB push_back
#define MP make_pair
int T,n;
char s[10000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);
    For(C,1,T)
    {
        scanf("%d",&n);
        scanf("%s",s);
        int ans=0;
        int cur=s[0]-'0';
        For(i,1,n)
        {
            if (cur<i)
            {
                ans+=i-cur;
                cur+=s[i]-'0'+i-cur;
            } else cur+=s[i]-'0';
        }
        printf("Case #%d: %d\n",C,ans);
    }


    return 0;
}
