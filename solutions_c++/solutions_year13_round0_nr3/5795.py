#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

typedef long long ll;

int rootpal[10000010];

bool ispal(ll n){
    if(n%10 == 0){
        return false;
    }
    ll a = 0, b = n;
    while(b > 0){
        a *= 10;
        a += b%10;
        b /= 10;
    }
    if(a == n){
        return true;
    }
    else{
        return false;
    }
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    memset(rootpal, 0, sizeof rootpal);
    rootpal[1] = 1;
    ll square;
    for(ll i = 2; i < 10000001; i++){
        if(ispal(i)){
            square = i*i;
            if(ispal(square)){
                rootpal[i]++;
            }
        }
        rootpal[i] += rootpal[i-1];
    }

    int n, a, b;
    double lower;
    cin >> n;
    for(int tc = 1; tc <= n; tc++){
        cin >> a >> b;
        lower = sqrt(a);
        a = ceil(lower) - 1;
        b = sqrt(b);
        printf("Case #%d: %d\n", tc, rootpal[b] - rootpal[a]);
    }

    return 0;
}
