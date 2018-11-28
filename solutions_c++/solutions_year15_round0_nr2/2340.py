// Author: Nguyen Duy Khanh
#include<bits/stdc++.h>
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define DEBUG(x) { printf << #x << " = " << x << endl; }
#define DEBUGARR(a,n) {cout << #a << " = " ; FOR(_,1,n) cout << a[_] << ' '; cout <<endl;}
#define CHECK printf("OK\n");
#define FILL(a, b) memset((a), (b), sizeof((a)))
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define Nmax 35000
using namespace std;

int res, nhom[1111], test, x, n, kk, a[1111], kq;

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    nhom[1] = 0;
    FOR(i,2,1000) {
        nhom[i] = 100000;
        FOR(j,1,i-1) nhom[i] = min(nhom[i], 1 + nhom[j] + nhom[i-j]);
    }

    cin >> test;
    FOR (d, 1, test){
        cin >> n;
        FOR(i,1,n) cin >> a[i];
        cout << "Case #" << d << ": ";
        res = 10000;
        kk = 0;
        FOR(i,1,n) kk = max(kk,a[i]);
        FOR(k,1,kk){
            kq = 0;
            FOR(i,1,n){
                if (a[i] <= k) continue;
                x = a[i] / k;
                if (a[i] % k != 0) x++;
                kq = kq + nhom[x];
            }
            res = min(res, k + kq);
        }
        cout << res << endl;
    }

    return 0;
}
