#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;
int g(int x)
{
    int num[10];
    for(int i=0;i<10;i++)num[i]=-1;
    int re=0;int ans=0;
    for(int i=1;;i++)
    {
        int now=x*i;ans=max(ans,now);
        while(now){
            if(num[now%10]==-1){
                num[now%10]=1;
                re+=now%10;
            }
            now/=10;
        }
        if(re==45&&num[0]==1){
            return ans;
        }
    }
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("out.txt", "w",stdout);
#endif
    int T;cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        cin>>n;
        if(n==0)printf("Case #%d: INSOMNIA\n",ca);
        else printf("Case #%d: %d\n",ca,g(n));
    }
    return 0;
}
