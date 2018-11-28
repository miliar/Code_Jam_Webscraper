#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

struct water
{
    double r, d;
    water(double r=0, double d=0) : r(r) , d(d){}
    
    bool operator<(const water& W) const
    {
        return d<W.d ;
    }
};

void solve()
{
    int n;
    double v, d;
    scanf("%d%lf%lf", &n, &v, &d);
    vector<water> a(n);
    
    for(int i=0; i<n; i++)
        scanf("%lf%lf", &a[i].r, &a[i].d);
    
    if( n==1 )
    {
        if( d==a[0].d )
            printf("%.8f\n", v/a[0].r);
        else
            printf("IMPOSSIBLE\n");
    }
    else
    {
        sort(a.begin(), a.end());
        
        if( d<a[0].d || d>a[1].d )
            printf("IMPOSSIBLE\n");
        else
        {
            if( a[0].d==a[1].d )
            {
                printf("%.8f\n", v/(a[0].r+a[1].r));
            }
            else
            {
                double diff=a[1].d-a[0].d;
                printf("%.8f\n", v*max((d-a[0].d)/(diff*a[1].r), (a[1].d-d)/(diff*a[0].r)));
            }
        }
    }
}

int main()
{
    for(int N, cases=scanf("%d", &N); cases<=N; cases++)
    {
        printf("Case #%d: ", cases);
        solve();
    };
}