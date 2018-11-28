//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

const int N = 2222222;
int lp[N+1];
vector<int> pr;
bool isPrime[N];

void getPrimes() {
    for (int i=2; i<=N; ++i) {
        if (lp[i] == 0) {
            lp[i] = i;
            pr.push_back (i);
        }
        for (int j=0; j<(int)pr.size() && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
            lp[i * pr[j]] = pr[j];
    }
    for(int i = 0; i < pr.size(); ++i) {
        isPrime[pr[i]] = 1;
    }
}

int dv[11];

int main() {
    getPrimes();
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int T = 1; T <= t; ++T) {
        int n, c;
        cin >> n >> c;
        cout << "Case #" << T << ":\n";
        for(int m = (1 << (n-1)); c > 0 && m < (1 << (n)); ++m) {
            if (m % 2 == 0) continue;
            
            bool flag = 1;
            string s = "";
            for(int o = 2; flag && o <= 10; ++o) {
                long long val = 0, st = 1;
                s = "";
                for(int i = 0; i < n; ++i) {
                    if ((m >> i) % 2 == 0)
                        s = "0" + s;
                    else {
                        s = "1" + s;
                        val += st;
                    }
                    st *= o;
                }
                if (val < N && isPrime[val]) { flag = 0; continue; };
                
                flag = 0;
                for(int i = 0; i < pr.size() && pr[i] * 1ll * pr[i] < val; ++i)
                    if (val % pr[i] == 0) {
                        dv[o] = pr[i];
                        flag = 1;
                        break;
                    }
            }
            
            
            if (flag) {
                cout << s;
                for(int i = 2; i <= 10; ++i)
                    cout << " " << dv[i];
                cout << "\n";
                c--;
            }
        }
        
    }
    return 0;
}