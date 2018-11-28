#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>

#define msn(x) (memset((x),0,sizeof((x))))
#define msx(x) (memset((x),0x7f,sizeof((x))))
#define fuck(x) cerr << #x << " <- " << x << endl
#define acer cout<<"sb"<<endl
typedef long long ll;
using namespace std;
#define inf 0x3f3f3f3f
#define eps 1e-8
#define pi acos(-1.0)
int p[1111];
int solve()
{
    int n;
    int d;
    scanf("%d",&n);
    priority_queue<int>q;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&p[i]);
    }

    int ans=1000;
    for(int i=1;i<=1000;i++)
    {
        int cmp=0;
        for(int j=0;j<n;j++)
        {
            cmp+=(p[j]+i-1)/i-1;
        }
        ans=min(i+cmp,ans);
    }
    return ans;
}
int main()
{
    freopen("bb.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: %d\n",cas,solve());
    }
}
