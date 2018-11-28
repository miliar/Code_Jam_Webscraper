#include <bits/stdc++.h>
using namespace std;
int tab[1003];
int main() {
    int t;
    cin >> t;
    for(int T = 1; T <= t;  T++) {
        int n; cin >> n;
        
        for(int i = 0; i < n; i++) {
            cin >> tab[i];
        }
        int rekord = 1000000009;
        for(int a = 1; a <= 1000; a++) {
            int licz = 0;
            for(int i = 0; i < n; i++) {
                licz += (tab[i]-1) / a;
            }
            rekord = min(rekord, a + licz);
        }
        printf("Case #%d: %d\n", T, rekord);
    }
    return 0;
}