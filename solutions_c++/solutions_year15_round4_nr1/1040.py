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

int test, n, m, res;
string a[111];

bool trong(int x, int y){
    if (x < 0 || y < 0 || x >= m || y >= n) return false;
    return true;
}

bool out(int x, int y){
    int kx, ky;
    kx = 0;
    ky = 0;
    if (a[x][y] == '^') kx = -1;
    if (a[x][y] == 'v') kx = 1;
    if (a[x][y] == '>') ky = 1;
    if (a[x][y] == '<') ky = -1;

    bool res = true;
    while (trong(x,y) == true){
        x = x + kx;
        y = y + ky;
        if (trong(x,y) == false) break;
        if (a[x][y] != '.'){
            res = false;
            break;
        }
    }

    return res;
}

bool check(int x, int y){
    a[x][y] = 'v';
    if (out(x,y) == false) return false;
    a[x][y] = '^';
    if (out(x,y) == false) return false;
    a[x][y] = '<';
    if (out(x,y) == false) return false;
    a[x][y] = '>';
    if (out(x,y) == false) return false;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> test;
    FOR(t,1,test){
        cin >> m >> n;
        FOR(i,0,m-1) cin >> a[i];

        res = 0;
        FOR(i,0,m-1)
        FOR(j,0,n-1)
            if (a[i][j] != '.')
            if (out(i,j) == true){
                if (check(i,j) == true) res = -123456;
                res++;
            }

        cout << "Case #" << t << ": ";
        if (res < 0) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }

    return 0;
}
