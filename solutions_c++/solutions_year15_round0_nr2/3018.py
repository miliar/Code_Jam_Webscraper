#include <iostream>
#include <cstdio>

using namespace std;

int P[1005];
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int _T;
    scanf("%d", &_T);
    for (int T = 1; T <= _T; T++){
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%d", &P[i]);
        int ans = 10000, tmp;
        for (int i = 1; i < 1002; i++){
            tmp = 0;
            for (int j = 0; j < N; j++){
                if (P[j]<=i) continue;
                tmp += P[j]/i+(P[j]%i==0?0:1)-1;
            }
            ans = min(ans, tmp + i);
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
