#include <algorithm>
#include <iostream>
#include <cstring>
#include <complex>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <bitset>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#define umin( x, y ) x = min( x, y )

using namespace std;

typedef long long Lint;
typedef pair<int, int> ii;

const int maxn = 1010;

int ar[maxn];

void solve(){
    int n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        scanf("%d",&ar[i]);
    }
    int ret = 1e9;
    for(int x = 1; x <= 1000; x++){
        int t = x;
        for(int i = 0; i < n; i++){
            t += (ar[i] - 1) / x;
        }
        umin(ret, t);
    }
    printf("%d\n", ret);
}

int main(){
    int a;
    scanf("%d",&a);
    
    for(int i = 1; i <= a; i++){
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
