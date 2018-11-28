#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
long long s[40]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    int t;
    scanf("%d",&t);
    int cnt,tmp;
    for(int cases=1;cases<=t;cases++)
    {
        long long x,y;
        scanf("%lld%lld",&x,&y);
        int ans=0;
        if(x<=s[1])
            x=s[1];
        if(y>=s[39])
            y=s[39];
        for(int i=1;i<=39;i++)
        {
            if(x==s[i])
                ans++;
            if(x>=s[i])
            {
                cnt=i+1;
            }
        }
        for(int i=39;i>=1;i--)
        {
            if(y==s[i]&&x!=y)
                ans++;
            if(y<=s[i])
            {
                tmp=i-1;
            }
        }
        //printf("%lld %lld\n",s[cnt],s[tmp]);
        //printf("%d....%d\n",cnt,tmp);
        if(tmp-cnt>=0)
            ans+=(tmp-cnt+1);
        printf("Case #%d: ",cases);
        printf("%d\n",ans);
    }
    return 0;
}
