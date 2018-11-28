#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1100;

int a[MAXN], t, n;

void FileIO(){
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
}

int main(){
    FileIO();
    scanf("%d", &t);
    for (int k = 1; k <= t; ++k){
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        int sum = 0, tmp = 0, rate = 0;

        for (int  i = 1; i < n; ++i)
            if (a[i-1] > a[i]){
                tmp += (a[i-1]-a[i]);
                rate = max(rate, a[i-1] - a[i]);
            }
        sum = tmp;

        tmp = 0;
        for (int i = 1; i < n; ++i)
            tmp += min(a[i-1], rate);
        printf("Case #%d: %d %d\n", k, sum, tmp);
    }
    return 0;
}
