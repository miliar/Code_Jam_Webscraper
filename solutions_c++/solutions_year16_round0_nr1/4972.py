#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

long long solve(long long n) {
    if (n == 0) return -1;
    
    set<int> st;
    long long curN = n;
    
    while (st.size() != 10) {
        long long buf = curN;
        while (buf != 0) {
            st.insert(buf % 10);
            buf /= 10;
        }
        curN += n;
    }
    
    return curN - n;
}

int main() {
    int t;
    
    cin >> t;
    for (int x=0;x<t;x++) {
        int n;
        cin >> n;
        long long res = solve(n);
        if (res == -1) cout << "Case #" << x+1 << ": " << "INSOMNIA" << "\n";
        else cout << "Case #" << x+1 << ": " << res << "\n";
    }
    
    return 0;
}

