#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

long long checkPrime(long long n) {
    for (long long i=2; i < sqrt(n); i++)
        if (n % i == 0) {
            return i;
        }
    return 0;
}

long convertBase2To(long long n, long base) {
    long long result = 0;
    long power = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            result += power;
        }
        n /= 2;
        power *= base;
    }
    return result;
}

int main() {
    ifstream fi("c.in");
    ofstream fo("c.out");
    
    int t;
    fi >> t;
    
    for (int i(0); i<t; i++) {
        int n, j;
        fi >> n >> j;
        
        vector< pair<long long, vector<long long>>> result(j);
        
        long long max_val = (1 << n) - 1;
        long long min_val = (1 << (n - 1)) + 1;
        int count = 0;
        for (long long x = min_val; x <= max_val; x += 2) {
            long long d = checkPrime(x);
            if (d == 0) {
                continue;
            }

            vector<long long> divisor(11, 0);
            divisor[2] = d;
            bool flag = true;
            
            for (long k=3; k <= 10; k++) {
                long long v = convertBase2To(x, k);
                d = checkPrime(v);
                if (d == 0) {
                    flag = false;
                    break;
                }
                divisor[k] = d;
            }
            if (flag) {
                result[count] = make_pair(x, divisor);
                count++;
                if (count == j) {
                    break;
                }
            }
        }
        fo << "Case #" << i + 1 << ":" << endl;
        for (int k=0; k<j; k++) {
            long x = result[k].first;
            for (int v=n-1; v>=0; v--) {
                fo << ((x >> v) & 1);
            }
            for (int v=2; v<=10; v++) {
                fo << " " << result[k].second[v];
            }
            fo << endl;
        }
    }
    
    fi.close();
    fo.close();
    return 0;
}