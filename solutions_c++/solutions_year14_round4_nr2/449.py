#include <cstdio>
#include <algorithm>
using namespace std;

int a[1000];

int solve(){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        scanf("%d", a + i);
    int cnt = 0, l = 0, r = n;
    while(l + 1 != r){
        int *x = min_element(a + l, a + r);
        if(x - a < (l + r) / 2) { // left half
            cnt += x - a - l;
            rotate(a + l, x, x + 1);
            l++;
        } else { // right half
            cnt += (r - l - 1) - (x - a - l);
            rotate(x, x + 1, a + r);
            r--;
        }
    }
    return cnt;
}

int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        printf("Case #%d: %d\n", i, solve());
    }
}
