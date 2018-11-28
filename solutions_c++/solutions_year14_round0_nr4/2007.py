#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

void solve(void){
    int N;
    scanf("%d", &N);
    double arr1[1010], arr2[1010];
    for(int i = 0; i < N; i++)
        scanf("%lf", &arr1[i]);
    for(int i = 0; i < N; i++)
        scanf("%lf", &arr2[i]);
    sort(arr1, arr1+N);
    sort(arr2, arr2+N);
    int war, d_war;
    war = d_war = 0;
    int used[1010];
    for(int i = 0; i < N; i++) used[i] = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++)
            if(!used[j] && arr1[i]<arr2[j]){
                war++;
                used[j] = 1;
                break;
            }
    }
    for(int i = 0; i < N; i++) used[i] = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++)
            if(!used[j] && arr2[i]<arr1[j]){
                d_war++;
                used[j] = 1;
                break;
            }
    }
    printf("%d %d\n", d_war, (N-war));
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
