#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include<iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int f[20];
int n;
int x,r;
int tmp;
int ans;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        memset(f,0,sizeof(f));
        tmp=0;
        scanf("%d",&r);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&x);
                if(i==r) f[x]++;
            }
        }
        scanf("%d",&r);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&x);
                if(i==r) f[x]++;
            }
        }
        for(int i=1;i<=16;i++)
        if(f[i]==2) {tmp++;ans=i;}
        if(!tmp) printf("Case #%d: Volunteer cheated!\n",++cas);
        else if(tmp>1) printf("Case #%d: Bad magician!\n",++cas);
        else printf("Case #%d: %d\n",++cas,ans);

    }

    return 0;
}
