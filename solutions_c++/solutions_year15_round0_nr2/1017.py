/**
country:China
Author:JiaYang Lee
Language:c++
Date:2015-04-11
School:SCAU
*/
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1050;
const int inf = 1e9+7;
const int mod = 1e9+7;
typedef long long ll;

int cas=1;
int n,data[N];

int calc(int x,int base,int &mx)
{
    int ans=0;
    ans=base/x-1;
    if(base%x)ans++;
    if(base<x)x=base;
    mx=max(x,mx);
    return ans;
}

int calcTime(int base)
{
    int ans=0,mx=0;
    for(int i=0;i<n;i++)
        ans+=calc(base,data[i],mx);
    return ans+mx;
}

void solve()
{
    printf("Case #%d: ",cas++);
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%d",&data[i]);
    int ans=1e9;
    for(int i=1;i<=1050;i++)
        ans=min(ans,calcTime(i));
    printf("%d\n",ans);
}

int main()
{
#ifdef LOCAL
    freopen("in","r",stdin);
    freopen("out","w",stdout);
#endif // LOCAL
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
    return 0;
}
