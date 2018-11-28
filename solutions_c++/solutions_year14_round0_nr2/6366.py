#include <iostream>
#include <cstdio>
using namespace std;

#define ll                      long long

#define inc(i,a,b)              for(int i=a;i<=b;++i)
#define dec(i,a,b)              for(int i=a;i>=b;--i)

const double eps = 1e-9;

int main() {
    ios::sync_with_stdio(false);
    
    int T; cin >> T;
    inc(t,1,T) {
        double c, f, x;
        cin >> c >> f >> x;
        
        double z = x/c - 2/f;
        double k = (int)(z);
        
        if(z-k < eps) k = k-1;
        
        k = max((double)0,k);
        
        double ans = 0;
        inc(i,0,k-1) {
            ans += c/(2+i*f);
        }
        ans += x/(2+k*f);
        
        cout.precision(12);
        cout << "Case #" << t << ": " << ans << "\n";
    }
}