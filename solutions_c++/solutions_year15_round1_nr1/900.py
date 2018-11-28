#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

int res1,res2;
int p[1100];
int n;
int m;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).out","w",stdout);
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        res1 = res2 = m = 0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%d",&p[i]);
        for(int i=1;i<n;i++)
        {
            if(p[i]<p[i-1]) {res1 += p[i-1] - p[i];m=max(m,p[i-1]-p[i]);}
        }
        for(int i=1;i<n;i++)
        {
            if(p[i]) res2 += min(m,p[i-1]);
            else res2 += p[i-1];
        }
        printf("Case #%d: %d %d\n",++cas,res1,res2);
    }
    return 0;
}
