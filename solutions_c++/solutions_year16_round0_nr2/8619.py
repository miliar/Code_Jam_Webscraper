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

string s;
int f[111][2];
int test;

void xuly(){
    if (s[0] == '-'){
        f[0][0] = 0;
        f[0][1] = 1;
    }
    else {
        f[0][0] = 1;
        f[0][1] = 0;
    }
    FOR(i,1,s.length()-1)
        if (s[i] == '-') {
            f[i][0] = min(f[i-1][0], f[i-1][1] + 1);
            f[i][1] = min(f[i-1][1] + 2, f[i-1][0] + 1);
        }
        else {
            f[i][0] = min(f[i-1][0] + 2, f[i-1][1] + 1);
            f[i][1] = min(f[i-1][1], f[i-1][0] + 1);
        }
    cout << f[s.length()-1][1] << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    FOR(i,1,test){
        cin >> s;
        cout << "Case #" << i << ": ";
        xuly();
    }
    return 0;
}
