#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>

using namespace std;

const int M = 1000002013;

long long f1(long long n, long long k) {
    if (n == 0)
        return 0;
    if (k == 0)
        return 0;
    return (1ll << (n - 1)) + f1(n - 1, (k - 1) / 2);
}

long long f2(long long n, long long k) {
    return (1ll << n) - 1 - f1(n, (1ll << n) - 1 - k);
}

int main() {
    ifstream cin("/Users/mac/topcoder/input.txt");
    ofstream cout("/Users/mac/topcoder/output.txt");
    
    int NT, CT;
    cin >> NT;
    
    for (CT = 0; CT < NT; CT ++) {
        cout << "Case #" << (CT + 1) << ": ";
        
        long long n, p;
        cin >> n >> p;
        p--;
        
        long long l = 0, r = (1ll << n);
        while (l + 1 < r) {
            long long m = (l + r) / 2;
            if (f1(n, m) <= p) {
                l = m;
            } else {
                r = m;
            }
        }
        long long k1 = l;
        
        l = 0, r = (1l << n);
        while (l + 1 < r) {
            long long m = (l + r) / 2;
            if (f2(n, m) <= p) {
                l = m;
            } else {
                r = m;
            }
        }
        long long k2 = l;

        
        cout << k1 << " " << k2 << endl;
    }
    
    return 0;
}
