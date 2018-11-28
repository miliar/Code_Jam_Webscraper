#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

string s; 
const int MAXN = 1000 + 10; 
char ch; 
int v, ar, br, av, bv, ans1, ans2, ans, tests, test, Time, c, n, m, l, r, data; 
double a[MAXN], b[MAXN]; 

int min(int a, int b){ return a < b ? a : b; }

int main(){
    freopen("4.in","r",stdin); 
    freopen("4.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        ans1 = 0; ans2 = 0; 
        scanf("%d", &n); 
        for (int i = 0; i < n; ++i) scanf("%lf", &a[i]); 
        for (int j = 0; j < n; ++j) scanf("%lf", &b[j]); 
        sort(a, a+n);
        sort(b, b+n);
		
        // ans1: give away k elements
        for (int k = 0; k < n; ++k) {
            if (n - k < ans1) break; 

            ans = 0; 
            l = n - 1; 
            r = n - 1 - k; 
            while (l >= 0 && r >= 0) {
                if (a[l] > b[r]) {
                    ++ans;
                    --l; 
                    --r; 
                } else {
                    --r;
                }
            }
            if (ans > ans1) ans1 = ans; 
        }

        // ans2
        int k = 0; 
        l = 0; 
        r = 0; 
        while (l <= n-1 && r <= n-1) {
            if (b[r] > a[l]) {
                ++ans2; 
                ++l;
                ++r; 
            } else {
                ++r; 
            }
        }
        ans2 = n - ans2; 

        printf("Case #%d: %d %d\n", test, ans1, ans2);

        //for (int i = 0; i < n; ++i) printf("%.4f, ", a[i]); printf("\n");  
        //for (int j = 0; j < n; ++j) printf("%.4f, ", b[j]); printf("\n"); 
    }   
     
    return 0;  
}
