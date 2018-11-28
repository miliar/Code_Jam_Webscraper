#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAX_N 1000

int a[MAX_N + 1];

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    int test = 0;
    int i, n;
    long long ans1, ans2, tot;
    int maxi;
    while (t--) {
        cin >>n;
        
        ans1 = 0ll; ans2 = 0ll; tot = 0ll;
        maxi = 0;
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        for (i = 1; i < n; i++) {
            if (a[i] < a[i - 1]) {
                ans2 += (a[i - 1] - a[i]);
                //maxi =(a[i - 1] - a[i]);
                if (a[i - 1] - a[i] > maxi) {
                    maxi = a[i - 1] - a[i];
                }
            }
        }
        //maxi = a[n - 2] - a[n-1];
        if (maxi < 0) maxi = 0;
        for (i = 0; i < n - 1; i++) {
            //tot += a[i];
            if (a[i] >= maxi) {
                ans1 += maxi;
                //tot -= maxi;
            }
            else {
                ans1 += a[i];
                //tot = 0ll;
            }
        }
        
        //if (maxi == -100001) ans1 = 0ll;
        
        
        test++;
        cout << "Case #" << test << ": " << ans2 << " " << ans1 << endl;
    }
    
        return 0;
}


