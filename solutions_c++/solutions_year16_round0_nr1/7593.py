/**
country:China
Author:JiaYang Lee
Language:c++
Date:2015-08-20
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
const int N = 1e6+500;
const int inf = 1e9+7;
const int mod = 1e9+7;
const double pi = acos(-1.0);
const double eps = 1e-9;
typedef long long ll;


bool vis[10];

bool allVisit()
{
    for(int i=0;i<10;i++)if(!vis[i])return false;
    return true;
}

void calc(int x)
{
    while(x)
    {
        vis[x%10]=true;
        x/=10;
    }
}

void solve()
{
    static int cas =1;

    int n;
    scanf("%d",&n);
    if(n==0)
    {
        printf("Case #%d: INSOMNIA\n",cas++);
        return;
    }
    memset(vis,0,sizeof vis);

    int ans=0;
    while(!allVisit())
    {
        ans++;
        calc(ans*n);
    }
    printf("Case #%d: %d\n",cas++,ans*n);
}

int main()
{

#ifdef  LOCAL
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // LOCAL
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
    return 0;
}
