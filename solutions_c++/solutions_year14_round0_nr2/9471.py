#include <iostream>
#include <math.h>
#include <algorithm>
#include <memory.h>

using namespace std;

double ans;

double ok(int mid, double c, double f, double x)
{
    double tot = 0.0;
    for(int i = 0; i < mid; i++)    tot += c/(f*i+2);
    tot += x/(f*mid+2);
    return tot;
}
int main()
{
   // freopen("q.in","r",stdin);
    freopen("output.out","w",stdout);
    double c, f, x, t;
    ans = 1 << 30;
    //cout << ok(3,500,4,2000) << endl;
    cin >> t;

    for(int i = 1; i <= t; i++)
    {
        cin >> c >> f >> x;
        ans = 0;
        cout << "Case #" << i << ": ";
        int l = 0, r = 10000001;
        while(l < r)
        {
            int mid = (l+r) / 2;
            if(ok(mid,c,f,x) < ok(mid+1,c,f,x)) ans = mid, r = mid;
            else l = mid + 1, ans = mid + 1;
        }
        cout.precision(7);
        cout << fixed << ok(ans,c,f,x) << endl;
    }
    return 0;
}
