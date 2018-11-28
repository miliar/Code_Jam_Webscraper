#include <cstdio>
#include <algorithm>
using namespace std;

int s[10000];

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        int n, x;
        scanf("%d %d", &n, &x);
        for(int j = 0; j < n; j++)
            scanf("%d", s + j);
        sort(s, s + n);
        int cnt = 0;
        for(int j = 0, k = n - 1; j <= k;) {
            if(s[j] + s[k] <= x)
                cnt++, j++, k--;
            else
                cnt++, k--;
        }
        printf("Case #%d: %d\n", i, cnt);
    }
}
