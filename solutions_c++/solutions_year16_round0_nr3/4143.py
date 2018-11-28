#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

long long conv(vector<int> v, long long base) {
    long long res = 0, k = 1;
    
    for (int i=v.size()-1;i>=0;i--) {
        res += v[i] * k;
        k *= base;
    }
    
    return res;
}

long long isPrime(long long val) {
    int n = sqrt(val);
    
    for (int i=2;i<=n;i++) {
        if (val % i == 0) return i;
    }
    
    return -1;
}

vector<long long> check(vector<int> v) {
    vector<long long> divs;
    
    for (int i=2;i<=10;i++) {
        long long div = isPrime(conv(v, i));
        if (div == -1) {
            divs.clear();
            return divs;
        } else divs.push_back(div);
    }
    
    return divs;
}

void solve(int n, int k) {
    vector<int> v;
    
    v.push_back(1);
    for (int i=2;i<n;i++) {
        v.push_back(0);
    }
    v.push_back(1);
    
    int m = pow(2, n-2);
    
    for (long i=0;i<m;i++) {
        int buf = i;
        for (int j=1;j<n-1;j++) {
            v[j] = buf % 2;
            buf /= 2;
        }
        
        vector<long long> divs = check(v);
        
        if (!divs.empty()) {
            k--;
            for (int j=0;j<n;j++) {
                cout << v[j];
            }
            cout << " ";
            for (int j=0;j<9;j++) {
                cout << divs[j] << " ";
            }
            cout << "\n";
            
            if (k == 0) return;
        }
    }
}

int main() {
    int t;
    
    cin >> t;
    for (int x=0;x<t;x++) {
        int n, j;
        
        cin >> n >> j;
        cout << "Case #" << x+1 << ":\n";
        solve(n, j);
        cout << "\n";
    }
    
    return 0;
}

