#include <bits/stdc++.h>
using namespace std;

#define ll long long
set<int>s;

void countDigit(ll num) {
    while(num) {
        int p = num % 10;
        num /= 10;
        s.insert(p);
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int test;
    cin >> test;
    for(int tc = 1; tc <= test; tc++) {
        ll N;
        cin >> N;
        if(N==0) cout << "Case #" << tc << ": INSOMNIA\n";
        else {
            int i = 1;
            while(1) {
                ll P = N * i++;
                countDigit(P);
                if(s.size()==10) {
                    cout << "Case #" << tc << ": " << P << "\n";
                    s.clear();
                    break;
                }
            }
        }
    }
    return 0;
}
