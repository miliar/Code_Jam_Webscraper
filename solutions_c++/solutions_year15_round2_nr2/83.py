#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int res;
int n, m, k;
int nm;

int f(int c1, int c2, int c3, int k, int cc = 0){
    int res = 0;
    //cout << c1 << " " << c2 << " " << c3 << endl;
    if (k <= c1) return 0;
    k -= c1;
    if (k <= cc) return k;
    k -= cc; res += cc;
    if (k <= c2) return k*2+res;
    res += c2*2; k -= c2;
    if (k <= c3) return k*3+res;
    res += c3*3; k -= c3;
    return res + k*4;
}

void solve(){
    cin >> n >> m >> k;
    nm = n*m;
    if (n > m) swap(n,m);
    if (n == 1){
        if (m%2 == 0) cout << f(nm/2,nm/2-1,0,k,1) << endl;
        else          cout << min(f(nm/2+1, nm/2,0,k), f(nm/2, nm/2-1, 0, k, 2)) << endl;
        return;
    }
    if (n%2 == 0 && m%2 == 0) cout << f(nm/2,2,(n/2-1+m/2-1)*2,k) << endl;
    if (n%2 == 0 && m%2 == 1) cout << f(nm/2,2,(n/2-1)*2+(m+1)/2-2+m/2,k) << endl;
    if (n%2 == 1 && m%2 == 0) cout << f(nm/2,2,(m/2-1)*2+(n+1)/2-2+n/2,k) << endl;
    if (n%2 == 1 && m%2 == 1) cout << min(f(nm/2+1,0,(n/2+m/2)*2,k),f(nm/2,4,(n/2+m/2)*2-4,k)) << endl;
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
