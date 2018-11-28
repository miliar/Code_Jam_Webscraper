#include <algorithm>
#include <iostream>

using namespace std;

int A[1002];
int a[1200];


int main(int argc, const char * argv[]) {
    freopen("B-large.in", "r",stdin);
    freopen("B-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int n = 1; n <= T; n++) {
        int D, t = 0, mx = 0;
        cin >> D;
        for (int i = 0; i < D; i++) {
            cin >> t;
            A[i] = t;
            if (A[i] > mx) mx = A[i];
        }
        
        int mn = mx;
        int sum = 0;
        for (int i = 1; i <= mx; i++) {
            sum = i;
            for (int j = 0 ; j < D ; j++) {
                if (A[j] > i) {
                    if(A[j]%i == 0)
                        sum += (A[j]/i-1) ;
                    else
                        sum += (A[j]/i) ;
                }
            }
            mn = min(mn, sum) ;
        }
        
        cout << "Case #" << n << ": " << mn << endl;
    }
    
    return 0 ;
}
