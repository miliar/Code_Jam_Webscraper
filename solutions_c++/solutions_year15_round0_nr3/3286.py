#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

string s;
int n, x;
int pf[1000500], sf[1000500];

int val(char c){
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
    return 1;
}
int mul(int a, int b){
    if (a == 1 || b == 1) return a*b;
    if (a == b) return -1;
    if (a == 2){
        if (b == 3) return 4;
        if (b == 4) return -3;
    }else
    if (a == 3){
        if (b == 2) return -4;
        if (b == 4) return 2;
    }else 
    if (a == 4){
        if (b == 2) return 3;
        if (b == 3) return -2;
    }
    return 1;
}
int mult (int a, int b){
    int ret = 1;
    if (a < 0) ret = -1, a = -a;
    if (b < 0) ret *= -1, b = -b;
    return mul(a,b)*ret;
}

string t;

void solve(){
    cin >> n >> x;
    int nn = n;
    n *= x;
    cin >> s;
    t = s;
    pf[0] = val(s[0]);
    for (int i = 1; i < n; i++)
        pf[i] = mult(pf[i-1], val(s[i%nn]));
    sf[n-1] = val(s[(n-1)%nn]);
    for (int i = n-2; i >= 0; i--)
        sf[i] = mult(val(s[i%nn]), sf[i+1]);
    int cur;
    for (int i = 0; i < n; i++){
        if (pf[i] == 2){
            cur = val(s[(i+1)%nn]);
            for (int j = i+2; j < n; j++){
               // printf("[%d-%d, %d-%d, %d-%d]\n", 1,i+1,i+2,j,j+1,n+1);
                if (cur == 3 && sf[j] == 4){
                    cout << "YES\n";
                    return;
                }
                cur = mult(cur, val(s[j%nn]));
            }
        }
    }
    cout << "NO\n";
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
