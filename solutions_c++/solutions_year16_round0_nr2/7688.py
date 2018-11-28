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



char ch[105];


void solve()
{
    scanf("%s",ch);
    int ans=0;
    int n=strlen(ch);
    for(int i=n-1;i>=0;i--)
    {
        if( (ans&1)^(ch[i]=='-')  )
        {
            ans++;
        }
    }
    static int cas=1;
    printf("Case #%d: %d\n",cas++,ans);
}

int main()
{
#ifdef LOCAL
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif // LOCAL
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
    return 0;
}
