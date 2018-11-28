#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

long long indep(long n, long long pos) {
    long cnt = 0;
    long long d = pos;
    
    while (d) {
        cnt++;
        d = (d - 1) / 2;
    }
    
    long long ans = 0;
    for (long i = n-cnt; i < n; ++i)
        ans += 1ll << (long long)i;
    
    return ans;
}

long long dep(long n, long long pos) {
    long cnt = 0;
    long long d = (1ll << (long long)n) - pos - 1ll;
    
    while (d) {
        cnt++;
        d = (d - 1) / 2;
    }
    
    long long ans = 0;
    for (long i = 0; i < n-cnt; ++i)
        ans += 1ll << (long long)i;
    
    return ans;
}

int main(int argc, char** argv) {
   freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    long T;
    cin >> T;

    for (long t = 0; t < T; ++t) {
        long n;
        long long p, ans1, ans2;
        cin >> n >> p;
        
        long long l = 0ll, m,  r = 1ll << (long long)n; // indep
        
        while (l + 1ll != r) {
            m = (l + r) / 2ll;
            
            if (indep(n, m) < p)
                l = m;
            else
                r = m;
        }
        ans1 = l;
        
        
        l = 0ll;
        r = 1ll << (long long)n;
        
        while (l + 1ll != r) {
            m = (l + r) / 2ll;
            
            if (dep(n, m) < p)
                l = m;
            else
                r = m;
        }
        ans2 = l;
        
        cout << "Case #" << t+1 << ": " << ans1 << " " << ans2 << "\n"; 
    }
    
    return 0;
}

