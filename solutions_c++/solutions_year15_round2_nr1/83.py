#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

long long n;
int d[2000];
int q[2000], ql,qr;
int tmp[1000], sz = 0;

long long inv(long long x){
    if (x%10 == 0) return x;
    long long r = 0;
    while (x) r = r * 10 + x%10, x /= 10;
    return r;
}

long long cnt(long long x){
   // cout << x << " 1\n";
    if (x < 100) return d[x];
    sz = 0;
    long long c = x, cc = 0;
    while (c) tmp[sz++] = c%10, c /= 10;
    for (int i = sz-1; i >= (sz+1)/2; i--) cc = cc*10 + tmp[i];
    for (int i = (sz+1)/2-1; i >= 0; i--) cc*= 10;
    cc++;
 //   cout << x << " " << cc << " " << x-cc+1 << endl;
    if (x > cc) return cnt(cc) + x-cc;
    if (inv(x) < x)  return cnt(inv(x))+1;
    return cnt(x-1)+1;
}

void solve(){
    cin >> n;
    cout << cnt(n) << endl;
}

int main()
{
    memset(d,-1,sizeof(d));
    d[1] = 1;
    ql = qr = 0;
    q[qr++] = 1;
    while (ql < qr && d[100] == -1){
       int v = q[ql++];
       if (d[v+1] == -1) {
            q[qr++] = v+1;
            d[v+1] = d[v] + 1;
       }
       int c = inv(v);
       while (d[c] == -1){
            q[qr++] = c;
            d[c] = d[v] + 1;
            c = inv(c);
       }
    }
 

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++)
        cout << "Case #" << tt << ": ", solve();
    
    return 0;
}
