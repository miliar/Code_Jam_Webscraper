#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int p[100005] ;
int n , ans ;

int main(){
    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;
    int _, cas = 0 ; scanf("%d", &_);
    while(_--) {
        scanf("%d", &n);
        for(int i = 0; i < n ; i++) scanf("%d", &p[i]);
        for(int i = 1 ; i <= 1000; i++) {
            int te = 0;
            for(int j = 0; j < n; j++)
                if(p[j] > i) {
                    te += p[j] / i;
                    if (!(p[j] % i)) te--;
                }
            if (i == 1) ans = te + i ;
            else ans = min(ans,  te + i);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
