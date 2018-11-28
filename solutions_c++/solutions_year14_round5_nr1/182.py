#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void read();
void kill();

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout.precision(11);
    cout << fixed;
    int t;

    cin >> t;

    for (int i = 1; i <= t; ++i){
        read();
        cout << "Case #" << i << ": ";
        kill();
    }

    return 0;
}

#define long long long

#define M 1000100

int n;
long p, q, r, s, a[M];


void read(){
    cin >> n >> p >> q >> r >> s;
    for (long i = 0; i < n; ++i)
        a[i] = (p*i + q) % r + s;
}

bool pos(long x){
    long sum = 0;
    long l = 0, k = 0;
    while (l < n){
        if (sum > x)
            return false;
        if (sum + a[l] > x){
            sum = 0;
            ++k;
        }
        sum += a[l];
        ++l;
    }

    if (sum > 0)
        ++k;
    if (sum > x)
        return false;
    return k <= 3;
}

void kill(){
    long l = 0, r = 1000000ll*1000000ll*10, m;
    while (l < r){
        m = (l + r) >> 1;
        if (pos(m))
            r = m;
        else
            l = m + 1;
    }
    long sum = 0;
    for (int i = 0; i < n; ++i)
        sum += a[i];

    cout << 1.0*(sum - l)/sum << "\n";
}
