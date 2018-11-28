#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

using namespace std;
#define equal(p,q) (((p)<(q)+0.00000001)&&((p)>(q)-0.00000001))

double vn[101];
double xn[101];


int solve() 
{
    int n;
    double v, x;
    cin>>n>>v>>x;
    //cout<<n<<"\t"<<v<<"\t"<<x<<endl;
    int i,j;
    for (i=0; i<n; i++) {
        cin>>vn[i]>>xn[i];
        //cout<<vn[i]<<"\t"<<xn[i]<<endl;
    }
    int poss = 1;
    double ans = 0.0;
    if (n == 1) {
        if (equal(xn[0],x)) {
            ans = v/vn[0];
        } else {
            poss = 0;
        }
    } else if(n==2) {
        if ((xn[0]<x-0.00000001 && xn[1]>x+0.00000001) || (xn[1]<x-0.00000001 && xn[0]>x+0.00000001)) {
            double tmp1 = (x-xn[0])/(xn[1]-xn[0]) * v/vn[1];
            double tmp0 = (v-tmp1*vn[1])/vn[0];
            //cout<<"tmp"<<tmp1<<"\t"<<tmp0<<endl;
            ans = tmp1>tmp0?tmp1:tmp0;
        } else if (equal(xn[0],x) && equal(xn[1],x)) {
            double tmp = vn[0]+vn[1]; 
            ans = v/tmp;
        } else if (equal(xn[0],x)) {
            ans = v/vn[0];
        } else if (equal(xn[1],x)) {
            ans = v/vn[1];
        } else {
            poss = 0;
        }
    }

    if (poss == 0) {
        cout<<"IMPOSSIBLE"<<endl;
    } else {
        cout.precision(9);
        cout<<fixed<<ans<<endl;
    }
    return 1;
}

int main() {
    int nc, tc;
    tc = 1;
    cin>>nc;
    while (tc<=nc) {
        cout<<"Case #"<<tc<<": ";
        solve();
        tc++;
    }
    return 0;
}
