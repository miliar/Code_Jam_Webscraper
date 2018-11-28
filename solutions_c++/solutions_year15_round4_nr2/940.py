#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>

#define X first
#define Y second
#define mp make_pair
#define pb push_back

typedef long long ll;

using namespace std;

int n;
double V, X;
double v[110], x[110];

void fail() {
    cout<<"IMPOSSIBLE"<<endl;
}

double bin(double st, double fin, int it) {
    if (it == 200) {
        return st;
    }
    double med = (st + fin)*0.5;
    double vol1 = med*v[1];
    double vol2 = V - vol1;
    if (vol1 * x[1] + vol2 * x[0] < X*V ) {
        return bin(med, fin, it + 1);
    }
    else {
        return bin(st, med, it + 1);
    }
}

void solve() {
    cin>>n>>V>>X;
    for (int i = 0; i < n; i++) {
        cin>>v[i]>>x[i];
    }
    if (n == 1) {
        if (x[0] != X) {
            fail();
        }
        else {
            cout<<V/v[0]<<endl;
        }
        return ;
    }
    if (x[0] > x[1]) {
        swap(x[0], x[1]);
        swap(v[0], v[1]);
    }
    if (x[1] < X || x[0] > X) {
        fail();
        return ;
    }
    if (x[0] == X && x[1] != X) {
        cout<<(V / v[0])<<endl;
        return ;
    }
    if (x[0] != X && x[1] == X) {
        cout<<(V / v[1])<<endl;
        return ;
    }
    if (x[0] == X && x[1] == X) {
        cout<<(V / (v[0] + v[1]) )<<endl;
        return ;
    }
    double t1 = bin(0.0, V / v[1], 0);
    double t2 = (V - t1 * v[1]) / v[0];
    cerr<<t1<<" "<<t2<<endl;
    cout<<max(t1, t2)<<endl;
}

int main() {
    cout<<fixed<<setprecision(8);
    freopen("Asm.txt", "r", stdin);
    freopen("Asm.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        printf("Case #%d: ", i );
        solve();
    }
	return 0;
}
