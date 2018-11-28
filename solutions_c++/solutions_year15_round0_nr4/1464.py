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

int test, x, n, m;

bool solve(int x, int n, int m){
    if (x == 1) return true;
    if (x == 2){
        if (n * m % 2 == 1) return false;
        else return true;
    }
    if (x == 3){
        if (n * m % 3 == 0 && n * m > 3) return true;
        else return false;
    }
    if (x == 4){
        if (n * m == 12 || n * m == 16) return true;
        else return false;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    FOR(d,1,test){
        cin >> x >> n >> m;
        cout << "Case #" << d << ": ";
        if (solve(x,n,m)) cout << "GABRIEL" << endl;
        else cout << "RICHARD" << endl;
    }

    return 0;
}
