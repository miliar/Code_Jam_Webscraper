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
const int maxm=1000005;
const int inf = 0x3fffffff;
const int mod = 1000000007;

double C,F,X;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,ncase=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        double ret=X/2,cur=0;
        for(int i=0; i<maxm; i++)
        {
            cur+=C/(2+i*F);
            double tt=cur+X/(2+(i+1)*F);
            ret=min(ret,tt);
        }
        printf("Case #%d: %.10f\n",++ncase,ret);
    }
    return 0;
}
