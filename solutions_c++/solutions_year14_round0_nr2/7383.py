#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

typedef double ld; //long double bug in win64 :(

ld C, F, X;

ld f(int n) { //n = how many farms
    ld ans = 0.;
    for (int i=0;i<n;++i) {
        ans += C/(2. + F*i);
    }
    ans+= X/(2.+F*n);
    return ans;
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    int t; cin >> t;
    for (int cas=1; cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        cin >> C >> F >> X;
        
        /*ld ans = f(0);
        int qq = 0;
        cout << 0 << " -> " << f(0) << endl;
        for (int i=1;i<10000;++i) {
            cout << i << " -> " << f(i) << endl;
            ld ret = f(i);
            if (ret < ans) {
                ans = ret;
                qq = i;
            }
        }
        cout << ans << endl;
        cout << " (( " << qq << endl;*/
        ld lo=0, hi = 1000000, m1,m2,x1,x2; //[lo, hi)
        while (hi-lo > 100) {
            //cerr << lo << ", " << hi << endl;
            m1 = (2.*lo + hi)/3.;
            m2 = (lo + 2.*hi)/3.;
            
            x1 = f(m1);
            x2 = f(m2);
            if (x1 < x2) hi=m2;
            else lo=m1;
        }
        
        ld ans = f(lo);
        int qq = lo;
        for (int i=lo;i<hi;++i) {
            //cout << i << " -> " << f(i) << endl;
            ld ret = f(i);
            if (ret < ans) {
                ans = ret;
                qq = i;
            }
        }
        cout << ans << endl;
        //cout << ans << " (" << qq << ")" << endl;
    }
}