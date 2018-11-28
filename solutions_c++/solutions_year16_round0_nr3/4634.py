#include<bits/stdc++.h>

using namespace std;

long long step, stepn, t, n, j, x, jj, numb;
bool y;

bool prost(long long x){
    for (long long i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

long long bin(long long x){
    long long m = 0;
    long long a[10000];
    while (x > 0){
        a[m] = x % 2;
        x = x / 2;
        m++;
    }
   // cout << a[0];
    long long ans = 0;
    for (long long i = m - 1; i > -1; i--){
        ans = ans * 10 + a[i];
    }
    return ans;
}
long long dec(long long x, long long y){
    long long t = 1;
    long long ans = 0;
    while (x > 0){
        ans += (x % 10) * t;
        t *= y;
        x = x / 10;
    }
    return ans;
}

main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    cin >> t;
    cin >> n >> jj;
    cout << "Case #1:" << endl;
    step = 1;
    stepn = 1;
    numb = 0;
    while (stepn < n){
        step *= 2;
        stepn++;
    }
    for (long long i = 1; i <= step; i++){
        if (i % 2 == 1){
            long long x = i + step;
            x = bin(x);
            //cout << x << endl;
            y = true;
            for (long long j = 2; j <= 10; j++){
                long long y1 = dec(x, j);
                //cout << y1 << " " << j << endl;
                if (prost(y1)){
                    y = false;
                    break;
                }
            }
          if (y) {
                cout <<  x << " ";
                for (long long j = 2; j <= 10; j++){
                long long y1 = dec(x, j);
                for (long long i = 2; i * i <= y1; i++)
                    if (y1 % i == 0) {cout << i << " "; break;}
          }
          cout << endl;
          numb++;
          if (numb == jj) return 0;
        }
    }
    }
}
