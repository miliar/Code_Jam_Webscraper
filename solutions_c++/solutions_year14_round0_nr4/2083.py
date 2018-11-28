#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define LL long long
using namespace std;

double a[1111];
double b[1111];

int main(){
    freopen ("D-large.in", "r", stdin);
    freopen ("D-large.out", "w", stdout);
    int t, n;
    int tt = 0;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) scanf("%lf", &a[i]);
        for(int i = 0; i < n; ++i) scanf("%lf", &b[i]);
        sort(a, a + n);
        sort(b, b + n);
        int ans1 = 0;
        int ans2 = 0;
        for(int i1 = 0, i2 = 0; i1 < n && i2 < n; ++i2, ++i1){
            while(i1 < n && a[i1] <= b[i2]) ++i1;
            if(i1 < n) ++ans1;
        }
        for(int i1 = 0, i2 = 0; i1 < n && i2 < n; ++i2, ++i1){
            while(i1 < n && b[i1] <= a[i2]) ++i1;
            if(i1 < n) ++ans2;
        }
        printf("Case #%d: %d %d\n", ++tt, ans1, n - ans2);
    }
	return 0;
}
