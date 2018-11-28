#include <iostream>
#include <math.h>
using namespace std;

bool isprime(unsigned long long n);

int main() {
    int T, N, J;
    //cin >> T;
    cout << "Case #1:" << endl;
    //cin >> N >> J;
    N = 16, J = 50;
    unsigned long long num[33], prime[11], p2[11], pw[11][33];
    for (int i=0; i<11; i++) {
        for (int j=0; j<33; j++) {
            pw[i][j] = pow(i,j);
        }
    }
    for (int n=0; n<33; n++) num[n] = 0;
    num[0] = num[N-1] = 1;
    for (int jj=0; jj<J; jj++) {
        unsigned long long x, i, cnt;
        do {
            for (int nn=0; nn<11; nn++) {prime[nn]=0;}
            cnt = 0;
            num[1]++;
            for (int n=1; n<N; n++) {
                if (num[n]==2) {
                    num[n+1]++;
                    num[n]=0;
                }
            }
            for (i = 10; i>=2; i--) {
                x=0;
                for (int n=0; n<N; n++) x+=num[n]*pw[i][n];
                p2[i]=x;
                if (!isprime(x)) {
                    for (int k=2; k<x; k++) {
                        if (x%k == 0) {
                            prime[i] = k;
                            cnt++;
                            break;
                        }
                    }
                } else break;
            }
        } while (cnt < 9 && num[N-1]==1);
        
        for (int n=N-1; n>=0; n--) cout << num[n];
        for (i = 2; i<=10; i++) cout << " " <<prime[i];
        cout << endl;
    }
}

bool isprime(unsigned long long n) {
    if (n == 2 || n ==3) return true;
    if (n % 2 ==0 || n % 3 ==0 ) return false;

    unsigned long long i = 5;
    unsigned long long w = 2;

    while (i * i <= n) {
        if (n % i == 0) return false;
        i += w;
        w = 6 - w;
    }
    return true;
}