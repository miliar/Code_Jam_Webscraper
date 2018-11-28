#include<bits/stdc++.h>

using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define ll long long

#define eps 1.0e-7

int main()
{
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        int n;
        double v,x;
        scanf("%d%lf%lf",&n,&v,&x);

        if(n==1) {
            double r,c;
            scanf("%lf%lf",&r,&c);
            if(c==x) {
                printf("Case #%d: %.9lf\n",tt,v/r);
                continue;
            }
            else {
                printf("Case #%d: IMPOSSIBLE\n",tt);
                continue;
            }
        }
        double r1,c1,r2,c2;
        scanf("%lf%lf%lf%lf",&r1,&c1,&r2,&c2);

        if(c1==x && c2==x) {
            printf("Case #%d: %.9lf\n",tt,v/(r1+r2));
            continue;
        }
        if(c1==x) {
            printf("Case #%d: %.9lf\n",tt,v/r1);
            continue;
        }
        if(c2==x) {
            printf("Case #%d: %.9lf\n",tt,v/r2);
            continue;
        }
        if(c1>x && c2>x) {
            printf("Case #%d: IMPOSSIBLE\n",tt);
            continue;
        }
        if(c1<x && c2<x) {
            printf("Case #%d: IMPOSSIBLE\n",tt);
            continue;
        }
        double v1=(x-c2)*v/(c1-c2);
        double v2=v-v1;
        if(v1>=0 && v2>=0)
            printf("Case #%d: %.9lf\n",tt,max(v1/r1,v2/r2));
        else
            printf("Case #%d: IMPOSSIBLE\n",tt);
    }
    return 0;
}
