#include <bits/stdc++.h>
using namespace std;
#define ll long long

int other(int a, int b) {
    for(int i = 2; i <= 4; ++i)
        if(i != a && i != b)
            return i;
    return -1;
}

int multiply(int a, int b) {
    int sign = 1;
    if(a * b < 0)
        sign = -1;

    a = abs(a), b = abs(b);
    int ans = 0;

    if(a == 1 || b == 1)
        ans = a * b;
    else if(a == b)
        ans = -1;
    else {
        if(a > b) {
            sign *= -1;
            swap(a, b);
        }
        if(b == a + 1)
            ans = other(a, b);
        else
            ans = -other(a, b);
    }

    return sign * ans;
}

int code(char c) {
    return c - 'i' + 2;
}

int raise(int a, ll b) {
    int ans = 1, by = a;

    for(ll i = 0; (1LL << i) <= b; ++i) {
        if((1LL << i) & b)
            ans = multiply(ans, by);
        by = multiply(by, by);
    }
    return ans;
}

int main() {
    
    ifstream cin("testC.in");
    ofstream cout("testC.out");

    int t; cin >> t;

    for(int tCase = 1; tCase <= t; ++tCase) {
        cout << "Case #" << tCase << ": ";
        ll n, x; cin >> n >> x;
        string A; cin >> A;
        int all = 1;

        for(int i = 0; i < n; ++i)
            all = multiply(all, code(A[i]));

        if(raise(all, x) != -1) {
            cout << "NO\n";
            continue;
        }

        string full;
        for(int i = 0; i < min(100LL, x); ++i)
            full += A;
        
        int tmp = 1, minI = 1e6, maxK = -1;

        for(int i = 0; i < (int) full.size(); ++i) {
            tmp = multiply(tmp, code(full[i]));
            if(tmp == 2)
                minI = min(minI, i);
            if(tmp == 4)
                maxK = max(maxK, i);
        }

        if(maxK > minI)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
}
