#include <iostream>
#include <cstdio>
#define SZ(X) ((int)((X).size()))
using namespace std;

int t, n, ans;
bool running;
string s;

inline void flip(int k){
    running = true, ans++;
    for (int i = 0; i < k-i; i++)
        swap(s[i], s[k-i]);
    for (int i = 0; i <= k; i++)
        s[i] = ((s[i] == '-') ? '+' : '-');
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    cin >> t;
    for (int q = 0; q < t; q++){
        cin >> s; ans = 0, n = SZ(s), running = true;
        while (running == true){
            running = false;
            if (s[0] == '-'){
                int p = 0;
                while (s[p] == '-')
                    p++;
                flip(p-1);
            }else{
                for (int i = 1; i < n; i++)
                    if (s[i] == '-'){
                        flip(i-1);
                        break;
                    }
            }
        }
        cout << "Case #" << q+1 << ": " << ans << "\n";
    }
    return 0;
}
