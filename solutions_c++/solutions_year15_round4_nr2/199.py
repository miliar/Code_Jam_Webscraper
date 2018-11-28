#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>
#define F first
#define S second

using namespace std;
const double E = 0.00000000001;
/*
double solve(double r0, double c0, double r1, double c1, double v, double x) {
    if(c0 < x && c1 < x) {
        return 1e200;
        goto ohi;
    }
    if(c0 > x && c1 > x) {
        return 1e200;
        goto ohi;
    }
    if(c1 == c0) {
       return v/(r0+r1);

    }
    else {
    double v1 = (x-c0)*v/(c1-c0);
    double v0 = v-v1;
    double ans = max(v0/r0, v1/r1);
        return ans;
    }
}
*/
int main() {
    int tt;
    cin>>tt;
    for(int i = 1; i <= tt; ++i) {
        cout<<"Case #"<<i<<": ";
        int n;
        double v, x;
        cin>>n>>v>>x;
        double vv = v;
        cout<<fixed;
        if(n == 1) {
            double r0, c0;
            cin>>r0>>c0;
            if(abs(c0-x) < E) {
                cout<<setprecision(15)<<v/r0<<'\n';
            }
            else {
                cout<<"IMPOSSIBLE\n";
                goto ohi;
            }
        }
        else if(n == 2) {
            double r0, c0, r1, c1;
            cin>>r0>>c0>>r1>>c1;
            if(c0 < x && c1 < x) {
                cout<<"IMPOSSIBLE\n";
                goto ohi;
            }
            if(c0 > x && c1 > x) {
                cout<<"IMPOSSIBLE\n";
                goto ohi;
            }
            if(c1 == c0) {
                cout<<setprecision(15)<<v/(r0+r1)<<'\n';

            }
            else {
            double v1 = (x-c0)*v/(c1-c0);
            double v0 = v-v1;
            double ans = max(v0/r0, v1/r1);
            cout<<setprecision(15)<<ans<<'\n';
            }
        }
        else {
            double ans = 1e200;
            vector<pair<double, double> > v(n);
            for(int i = 0; i < n; ++i) {
                cin>>v[i].S>>v[i].F;
            }
            sort(v.begin(), v.end());
            for(int i = 0; i < n; ++i) {
                for(int j = i; j < n; ++j) {
                    double flow = 0;
                    double temp = 0;
                    double yl = 0;
                    for(int k = i; k <= j; ++k) {
                        flow += v[k].S;
                        yl += v[k].F*v[k].S;
                    }
                    temp = yl / flow;
                    if(abs(temp-x) < E) {
                        ans = min(ans, vv/flow);
                    }
                    for(int k = 0; k < n; ++k) {
                        if(k > j || k < i) {
                            if(abs(temp-v[k].F) > E) {
                                double f2 = (x-temp)*flow/(v[k].F - x);
                                if(f2 <= v[k].S && f2 >= 0) {
                                    ans = min(ans, vv/(flow+f2));
                                }
                            }
                        }
                    }
                }
            }
            if(ans > 1e199) {
                cout<<"IMPOSSIBLE\n";
            }
            else {
                cout<<fixed;
                cout<<setprecision(15)<<ans<<'\n';
            }
        }
        ohi:;
    }

}
