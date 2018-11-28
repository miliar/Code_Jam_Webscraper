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
#define Nmax 100100
using namespace std;

bool f[10];
int test;
long long n, x;

void tach(int n){
    while (n > 0){
        f[n%10] = true;
        n /= 10;
    }
}

bool check(){
    FOR(i,0,9)
        if (f[i] == false) return false;
    //FOR(i,0,9) cout << f[i] << " "; cout << endl;
    return true;
}

void xuly(){
    if (n == 0){
        cout << "INSOMNIA" << endl;
        return;
    }
    FOR(i,0,9) f[i] = false;
    x = 0;
    while(1){
        x += n;
        tach(x);
        if (check()) {
            cout << x << endl;
            return;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    FOR(i,1,test){
        cin >> n;
        cout << "Case #" << i << ": ";
        xuly();
    }
    return 0;
}
