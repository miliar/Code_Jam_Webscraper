#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
#include<cstdlib>
#include<queue>
#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;

#define N 1000005
#define L(x) x<<1
#define R(x) x<<1|1
#define M(x,y) (x + y)>>1
#define MOD 1000000007
#define MODD 1000000006
#define inf 0x7fffffff
#define llinf 0x7fffffffffffffff
#define LL long long

int s[5][5];
int mark[20];
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int i,j,k,l;
    int t,test = 1,n,m;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        memset(mark,0,sizeof(mark));
        for(i = 1;i <= 4;i++)
        {
            for(j = 1;j <= 4;j++)
            {
                scanf("%d",&s[i][j]);
                if(i == n)
                    mark[s[i][j]] = 1;
            }
        }
        scanf("%d",&m);
        int ans = 0,flag;
        for(i = 1;i <= 4;i++)
        {
            for(j = 1;j <= 4;j++)
            {
                scanf("%d",&s[i][j]);
                if(i == m && mark[s[i][j]])
                    ans++,flag = s[i][j];
            }
        }
        if(ans == 0)
            printf("Case #%d: Volunteer cheated!\n",test++);
        else if(ans == 1)
            printf("Case #%d: %d\n",test++,flag);
        else
            printf("Case #%d: Bad magician!\n",test++);
    }
    return 0;
}
