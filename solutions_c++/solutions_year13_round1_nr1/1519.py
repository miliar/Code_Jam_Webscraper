#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
    if(fopen("in.in","r")) {
        freopen("in.in","r",stdin);
        freopen("out.out","w",stdout);
    }
    int c1;
    long long r, t, k;
    cin >> c1;
    for(int i=1; i<=c1; i++) {
        cin >> r >> t;
        k = (int) (-(2*r-1) + sqrt((2*r-1)*(2*r-1) + 4*(t)*2));
        k /= 4;
        if(k<0) {k=0;}
        cout << "Case #" << i << ": " << k << "\n";
    }
    return 0;
}
