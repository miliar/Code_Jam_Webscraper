#include <cstdio>
#include <algorithm>
using namespace std;

int T,D;
int ds[1010];
int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%d", &D);
        int maxD = 0;
        for(int i = 0; i < D; i++){
            scanf("%d", ds+i);
            maxD = max(maxD, ds[i]);
        }
        int ans = maxD;
        for(int i = 1; i <= maxD; i++){
            int m = 0;
            for(int j = 0; j < D; j++){
                m += (ds[j]+i-1)/i - 1;
            }
            ans = min(ans, m+i);
        }
        printf("Case #%d: %d\n",t,ans); 
    }
}

