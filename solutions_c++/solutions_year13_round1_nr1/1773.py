#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

long long int paintRequired(long long int r, long long int n) {
    n = 2 * n - 1;
    return (n * (n + 1) / 2 + r * (n + 1));
}

long long int approxN(long long int r, long long int t) {
    double a = 0.5;
    double b = r + 0.5;
    double c = r;
    
    return floor(((-b + sqrt(b * b - 4 * a * c))/(2 * a)) / 2 - 1);
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        long long int r;
        cin >> r;
        long long int t;
        cin >> t;
        
        long long int N = approxN(r, t);
        while (paintRequired(r, N) <= t)
            N++;
        N--;
        
        printf("Case #%d: %lld\n", i, N);
    }
    
    return 0;
}

