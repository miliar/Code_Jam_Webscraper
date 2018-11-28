#include <bits/stdc++.h>
using namespace std;

const int N = 1004;
int num[N], sum[N];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TC, tc, i, n, ans;
    scanf("%d", &TC);
    for(tc= 1;tc <= TC;tc++){
        scanf("%d", &n);
        ans = 0;
        for(i = 0; i <= n; i++){
            scanf("%1d", &num[i]);
        }
        sum[0] = num[0];
        for(i = 1; i <= n; i++){
            if(num[i] == 0){
                sum[i] = num[i] + sum[i-1];
                continue;
            }
            if(sum[i-1] < i){
                ans += i - sum[i-1];
                sum[i] =  i + num[i];
            }else{
                sum[i] = sum[i-1] + num[i];
            }
        }
        printf("Case #%d: %d\n",tc, ans);
    }
    return 0;
}
