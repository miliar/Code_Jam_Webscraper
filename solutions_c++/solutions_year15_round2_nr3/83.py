#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>


using namespace std;

int sz = 0;

class hiker{
    public:
    double v, x;
    hiker(){
    }
    hiker(int m, int d){
        x = d;
        v = 360.0 / double(m);
    }
    double pos(double t){
        return x + v*t;
    }
    double time(double pos){
        return (pos-x)/v;
    }
    bool operator < (const hiker &a) const{
        return v < a.v;
        //return x < a.x || (x == a.x && v > a.v);
    }
}a[100];

void solve(){
    int sp, k, mx, n;
    sz = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> sp >> k >> mx;
        for (int j = 0; j < k; j++){
            a[sz] = hiker(mx+j,sp);
            sz++;
        }
    }
    sort(a,a+sz);
    if (sz <= 1){
        cout << 0 << endl;
        return;
    }
    if (sz == 2){
        if (abs(a[0].v-a[1].v) < 1e-7){
            cout << 0 << endl;
            return;
        }
        double t1 = a[0].time(360);
        double t2 = a[1].time(360);
        if (a[1].pos(t1) < 720.0){
            cout << 0 << endl;
            return;
        }
        
        cout << 1 << endl;
    }
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
