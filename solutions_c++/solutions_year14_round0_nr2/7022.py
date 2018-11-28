#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

double c, f, x;

double check(int mid, double x)
{
    double tot = 0.0;
    for(int i = 0; i < mid; i++)    tot += c/(2.0+f*i);
    tot += x/((double)f*mid+2.0);
    return tot;
}

int main()
{
    freopen("Q2out.out", "w", stdout);
    int t, k;
    cin >> t;
    for(k = 1; k <= t; k++)
    {
        cin >> c >> f >> x;
        int L = 0, R = 10000000, ans = 0;
        while(L < R)
        {
            int mid = (L+R)/2;
            if(check(mid, x) < check(mid+1,x))  R = mid, ans = mid;
            else L = mid+1, ans = mid+1;
        }
        double tot = 0.0;
        for(int i = 0; i < ans; i++)    tot += c/(2.0+f*i);
        tot += x/((double)f*ans+2.0);
        printf("Case #%d: %.7lf\n", k, tot);
    }
    return 0;
}
