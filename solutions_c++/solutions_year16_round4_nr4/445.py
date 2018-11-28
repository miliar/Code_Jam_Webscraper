#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;
#define maxn 1000
char s[5][5];
int ans[5];
int num[5][32];
int main()
{
    freopen("D.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%s",s[i]);
            for(int j=0;j<n;j++) if(s[i][j]=='1') ans[i]^=(1<<j);
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<(1<<n)-1;j++)
            {
                bool sign=0;
                for(int k=0;k<n;k++)
                {
                    if((j&(1<<k)==0)&&(ans[i]&(1<<k)))
                    {
                        sign=1;
                    }
                    if((j&(1<<k))&&(ans[i]&(1<<k)==0))
                    {
                        num[i][j]++;
                    }
                }
                if(sign==1) num[i][j]=INF;
            }
        }

        printf("Case #%d: %d\n", cas, ans);
    }
}
