#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

vector<long long int> v;

int getDigit(int d, long long int k) { return k % int(pow(10.0, d+1)) / int(pow(10.0, d)); }

bool checkPalin(long long int k) {
     int digits = int(log10(k)) + 1;
     for ( int i = 0; i < digits; i++ ) {
         if ( getDigit(i, k) != getDigit(digits-1-i, k) ) return false;
     }
     return true;
}

int main() {
    freopen("C-small.txt", "r", stdin);
    freopen("C-small-out.txt", "w", stdout);
    int n;
    for ( long long int i = 0; i < 1005; i++ ) if ( checkPalin(i) ) if ( checkPalin(i*i) ) v.push_back(i*i);
    scanf("%d", &n);
    for ( int i = 0; i < n; i++ ) {
        long long int a, b;
        scanf("%lld%lld", &a, &b);
        printf("Case #%d: %d\n", i+1, upper_bound(v.begin(), v.end(), b)-lower_bound(v.begin(), v.end(), a));
    }
    return 0;
}
