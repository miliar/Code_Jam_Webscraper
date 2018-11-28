#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

const int N = 10010;

int n, p;
int a[N];
bool flag[N];

int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int _, cas = 1;
    for(scanf("%d", &_); _--; ){
        printf("Case #%d: ", cas++);
        scanf("%d %d", &n, &p);
        for(int i = 0; i < n; ++i) scanf("%d", a + i);
        sort(a, a + n);
        int ans = 0;
        memset(flag, false, sizeof(flag));
        for(int i = 0, j = n - 1; i < n; ++i, --j){
            if(flag[i]) continue;
            flag[i] = true;
            while(j >= 0 && a[i] + a[j] > p) j--;
            if(!flag[j]) flag[j] = 1;
            ans ++;
        }
        cout << ans << endl;
    }
    return 0;
}
