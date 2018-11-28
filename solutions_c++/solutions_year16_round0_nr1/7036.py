#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("output-large-A.txt", "w", stdout);
    int t;
    ll n;
    scanf("%d", &t);
    for(int j = 1; j <= t; j++) {
        scanf("%lld", &n);
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", j);
            continue;
        }
        set <int> s;
        int temp = n, i = 1;
        while(temp > 0) {
            s.insert(temp % 10);
            temp /= 10;
        }
        ll n1 = n;
        while(s.size() < 10) {
            i++;
            n = n1*i;
            temp = n;
            while(temp > 0) {
                s.insert(temp % 10);
                temp /= 10;
            }
        }
        cout << "Case #" << j << ": " << n << "\n";
    }
    return 0;
}

//g++ problema.cpp -std=c++11 -o problema