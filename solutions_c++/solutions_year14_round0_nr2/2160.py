#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
double C,F,X; // C buys farm, a farm gives F, X goal
double calc(int nfarm)
{
    double tm = 0;
    double per = 2;
    int i;
    for (i=1; i<=nfarm; ++i)
    {
        tm += C/per;
        per += F;
    }
    return tm + X/per;
}
double find()
{
    int low = 0, high = X + 1, mid1,mid2;
    double t1,t2;
    while (low < high)
    {
        mid1 = low + (high-low)/3;
        mid2 = low + ((high-low)*2)/3;
        t1 = calc(mid1), t2 = calc(mid2);
        if (t1 > t2) low = mid1+1;
        else high = mid2;
    }
    return calc(low);
}
int main()
{
    //freopen("data.txt", "r", stdin);
    freopen("Bin.txt", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int t,T;
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        printf("Case #%d: %.8lf\n", t, find());
    }
    return 0;
}
