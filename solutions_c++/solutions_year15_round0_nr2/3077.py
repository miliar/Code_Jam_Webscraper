#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, d, p[1005];
    scanf("%d",&T);
    for(int t = 1; t <= T; t++){
        scanf("%d",&d);
        for(int i = 0; i < d; i++)
            scanf("%d",&p[i]);
        int ans = 1000;
        for(int i = 1; i <= 1000; i++){
            int spc = 0;
            for(int j = 0; j < d; j++)
                spc += (p[j] / i) - (p[j] % i == 0);
            ans = min(ans, spc + i);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
