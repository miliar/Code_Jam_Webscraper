#include <iostream>
#include <cmath>

using namespace std;

#define square(a) a*a


int T = 0;
int i, j;


static void solve() {
    cout<< "Case #" << ++T << ": ";
    //int n, m; scanf("%d %d", &n, &m);
    int r,t; cin >> r >> t;
    //cout << "r=" << r << " t=" << ti << endl;

    int R = 2*r;
    
    //td = td * td;
    int count = 0;
    for (i = 1; t >= 0; i+=4) {
        int b = R + i;
        t -= b;
        count++;
    }
    count--;
    
    if (count == 0) count = 1;
    
    cout << count << endl;
}

int main(int argc, const char * argv[])
{
    int t = 0;
    cin >> t;
    
    //fr(i, t)
    for (int i = 0; i < t; i++) {
        solve();
    }
    return 0;
}
