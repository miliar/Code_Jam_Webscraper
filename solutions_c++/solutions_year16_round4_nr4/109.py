#include <cstdio>
#include <algorithm>
using namespace std;

int tc;
int n;
int a[5][5], ca[5][5];

bool f(int human, int mach){
    if(human == 0) return true;
    for(int i = 0; i < n; i++){
        if(human & (1 << i)){
            bool flag = false;
            for(int j = 0; j < n; j++){
                if(ca[i][j] && (mach & (1 << j))){
                    flag = f(human - (1 << i), mach - (1 << j));
                    if(!flag) break;
                }
            }
            if(!flag) return false;
        }
    }
    return true;
}


int main(){
    freopen("Ds.in", "r", stdin);
    freopen("Ds.out", "w", stdout);
    scanf("%d", &tc);
    for(int ttc = 1; ttc <= tc; ttc++){
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                scanf("%1d", a[i] + j);
            }
        }
        int ans = 30;
        for(int i = 0; i < (1 << (n * n)); i++){
            int cnt = 0;
            for(int j = 0; j < n; j++){
                for(int k = 0; k < n; k++){
                    ca[j][k] = a[j][k] || ((i & (1 << (j * n + k))) != 0);
                    if(ca[j][k] && !a[j][k]) cnt++;
                }
            }
            if(cnt >= ans) continue;
            //for(int k = 0; k < n; k++, puts("")) for(int j = 0; j < n; j++) printf("%d", ca[k][j]);
            if(f((1 << n) - 1, (1 << n) - 1)) ans = min(ans, cnt);
            //printf("///%d\n", f((1 << n) - 1, (1 << n) - 1));
        }
        printf("Case #%d: %d\n", ttc, ans);
    }
}
