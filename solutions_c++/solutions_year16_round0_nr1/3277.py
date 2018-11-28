#include<cstdio>
#include<cstdlib>
#include<time.h>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>

//#include<bits/c++std.h>

#define Size 1000005
#define inf 2e9
#define INF 2e18
#define LL long long int
#define i64 __int64
#define ULL unsigned long long
#define Mod 1000000007
#define pi 4*atan(1)
#define eps 1e-8
#define lson now*2,l,l+(r-l)/2
#define rson now*2+1,l+(r-l)/2+1,r
#define Max(a,b) (a)>(b)?(a):(b)
using namespace std;
int n,m,k;
int ql,qr,pos;
int vis[20];
int cnt = 0;

void judge(LL x)
{
    int tmp = 0;
    while(x)
    {
        tmp = x % 10;
        x /= 10;
        if(!vis[tmp])
        {
            vis[tmp] = 1;
            cnt++;
        }
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    int x,y,z;
    int Case=0;
    cin>>t;
    while(t--)
//    while(scanf("%d",&n)==1)
    {
        cin>>n;
        printf("Case #%d: ",++Case);
        if(n == 0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        cnt = 0;
        memset(vis,0,sizeof(vis));
        LL tmp = 0;
        LL sum = 0;
        for(int i=1;cnt<10;++i)
        {
            tmp = (LL)i*(LL)n;
            judge(tmp);
            sum++;
        }
        cout<<sum * (LL)n<<endl;
    }
    return 0;
}

