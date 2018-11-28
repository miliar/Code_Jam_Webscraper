#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>
#include <map>
#include <stack>
#include <iostream>
using namespace std;
typedef long long ll;
const double eps = 1e-8;
const double PI = acos(-1);
const int maxn = 5;
const int inf = 0x3fffffff;
const int mod = 1000000007;

int a[maxn][maxn],b[maxn][maxn];
vector<int>c;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,ncase=0;
    scanf("%d",&T);
    while(T--)
    {
        int l,r;
        scanf("%d",&l);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&r);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&b[i][j]);
        c.clear();
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            if(a[l][i]==b[r][j])c.push_back(a[l][i]);
        if(c.size()==0)printf("Case #%d: Volunteer cheated!\n",++ncase);
        else if(c.size()>1)printf("Case #%d: Bad magician!\n",++ncase);
        else printf("Case #%d: %d\n",++ncase,c[0]);
    }
    return 0;
}
