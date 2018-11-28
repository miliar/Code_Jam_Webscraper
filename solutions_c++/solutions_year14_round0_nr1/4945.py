#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
//#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#define REP(k,x,y) for(k=x;k<y;k++)
#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-9
#define ll long long
#define i64 __int64
#define INF 2000000000
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 10007
#define CLR(t,x) memset(t,x,sizeof(t));
#define N 500005
int mp[100];
int main()
{
    //freopen("E:\\A-small-attempt0.in","r",stdin);
    //freopen("E:\\A-small-attempt0.out","w",stdout);
    int cas,n,x,flag,cnt,tt=1;
    scanf("%d",&cas);
    while(cas--)
    {
        CLR(mp,0);
        scanf("%d",&n);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                scanf("%d",&x);
                if(i==n-1) mp[x]++;
            }
        scanf("%d",&n);
        cnt=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                scanf("%d",&x);
                if(i==n-1&&mp[x]) cnt++,flag=x;
            }
        printf("Case #%d: ",tt++);
        if(cnt==1) printf("%d\n",flag);
        else if(cnt>1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
