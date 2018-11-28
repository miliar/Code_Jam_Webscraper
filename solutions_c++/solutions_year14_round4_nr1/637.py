#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int a[10005];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T; cin >> T;
    int n,m;
    for (int o = 1; o <= T; o++){
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            scanf("%d", a + i);
        sort(a, a + n);
        int ans = 0;
        int i = 0;
        for (int j = n - 1; j >= 0; j--){
            if (j < i) break;
            if (a[j] + a[i] <= m){
                ans++;i++;
            } else ans++;
        }
        printf("Case #%d: %d\n", o, ans);
    }

}
