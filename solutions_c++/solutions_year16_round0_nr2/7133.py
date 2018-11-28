#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("output-large-B.txt", "w", stdout);
    int t;
    string a;
    cin >> t;
    for(int j = 1 ; j <= t; j++) {
        cin >> a;
        int len = a.length();
        bool minus = true;
        for(int i = 0; i < len ; i++) {
            if(a[i] == '+') {
                minus = false;
                break;
            }
        }
        if(minus) {
            cout << "Case #" << j << ": " << 1 << "\n";
            continue;
        }
        
        bool plus = true;
        for(int i = 0; i < len; i++) {
            if(a[i] == '-') {
                plus = false;
                break;
            }
        }
        if(plus) {
            cout << "Case #" << j << ": " << 0 << "\n";
            continue;
        }

        int ans = 0;
        int i = 0;
        while(a[i] == '-')
            i++;
        if(i != 0)
            ans = 1;
        i++;
        int count = 0;
        for(; i < len; i++) {
            bool flag = false;
            while(i < len && a[i] == '-') {
                i++;
                flag = true;
            }
            if(flag)
                ++count;
        }
        cout << "Case #" << j << ": " << ans + 2*count << "\n";
    }

    return 0;
}

//g++ problemb.cpp -std=c++11 -o problemb