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
const int N = 1e6+500;
const int inf = 1e9+7;
const int mod = 1e9+7;
typedef long long ll;

int cas=1;
char ch[1050];

void init()
{

}

void solve()
{
    printf("Case #%d: ",cas++);
    int n,ans=0,cnt=0;
    scanf("%d%s",&n,ch);
    cnt=ch[0]-'0';
    for(int i=1;i<=n;i++)
    {
        if(cnt<i)
        {
            ans+=i-cnt;
            cnt=i;
        }
        cnt+=ch[i]-'0';
    }
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
