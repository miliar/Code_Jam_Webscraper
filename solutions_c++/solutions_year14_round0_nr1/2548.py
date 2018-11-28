/// 优先队列 priority_queue
/// 全排列 next_permutation
#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>
#include<string>
#include<cstring>
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<set>
#include<ctime>
#include<cmath>
#define mmax  100010
#define eps 1e-8
#define ll __int64
#define ex 2.7182818284590452354
#define pi 3.141592653589793239
#define inf 0x7fffffff
#define DC(n) printf("Case #%d: ",++n)
#define SD(n) scanf("%d",&n)
#define SS(str) scanf("%s",str)
#define SDB(n) scanf("%lf",&n)
#define mm 1000000007
///#define debug
using namespace std;
int a[5][5];
int b[5][5];
int find(int x)
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(b[i][j]==x)
                return i;
        }
    }
}
int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    SD(t);
    int r1,r2,ca=0;
    while(t--)
    {
        SD(r1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                SD(a[i][j]);
        SD(r2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                SD(b[i][j]);
        r1--;
        r2--;
        int cnt=0;
        int ans;
        DC(ca);
        for(int i=0;i<4;i++)
        {
            int x=find(a[r1][i]);
            if(x==r2)
            {
                cnt++;
                ans=a[r1][i];
            }
        }
        if(!cnt)
            printf("Volunteer cheated!\n");
        if(cnt==1)
            cout<<ans<<endl;
        if(cnt>1)
            printf("Bad magician!\n");
    }
}
