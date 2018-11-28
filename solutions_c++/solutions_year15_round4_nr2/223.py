#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#define eps 1e-10
#define inf 1e20
using namespace std;
class tap
{
public:
    long double r, c;
    tap(){}
    tap(long double r, long double c):r(r), c(c){}
    bool operator<(const tap& t) const
    {
        return c>t.c;
    }
};
tap ts[101];
int main()
{
    int t;
    int cs=0;
    cin>>t;
    while (t--)
    {
        int n;
        long double v, x;
        cin>>n>>v>>x;
        for (int i=1; i<=n; i++)
        {
            long double r, c;
            cin>>r>>c;
            ts[i]=tap(r, c);
        }
        sort(ts+1, ts+n+1);
        long double time_max=inf;
        long double time_min=0;
        while (fabs(time_max-time_min)>eps)
        {
            long double time_mid=(time_max+time_min)/2;
            long double temp_max=0;
            long double volumn=v;
            bool fail=false;
            for (int i=1; i<=n; i++)
            {
                temp_max+=min(volumn, time_mid*ts[i].r)*ts[i].c;
                volumn-=min(volumn, time_mid*ts[i].r);
            }
            if (fabs(volumn)>eps||temp_max/v+eps<x) fail=true;
            long double temp_min=0;
            volumn=v;
            for (int i=n; i>=1; i--)
            {
                temp_min+=min(volumn, time_mid*ts[i].r)*ts[i].c;
                volumn-=min(volumn, time_mid*ts[i].r);
            }
            if (fabs(volumn)>eps||temp_min/v-eps>x) fail=true;
            if (fail) time_min=time_mid;
            else time_max=time_mid;
        }
        cout<<"Case #"<<++cs<<": ";
        if (time_min>inf/2||fabs(time_min)<eps) cout<<"IMPOSSIBLE\n";
        else cout<<fixed<<setprecision(8)<<time_min<<endl;
    }
    return 0;
}
