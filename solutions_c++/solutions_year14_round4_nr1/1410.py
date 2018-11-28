#include <cstdio>
#include <algorithm>
using namespace std;
const int MAX = 10004;
int v[MAX], used[MAX], N, X;
int main(){
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%d %d", &N, &X);
        for(int i = 0; i < N; i++){
                scanf("%d", v + i);
                used[i] = 0;
        }
        sort(v, v + N);
        int ans = 0, r = N - 1, l = 0;
        while(l < r){
            if(v[l] + v[r] <= X){
                //printf("%d %d\n", v[l], v[r]);
                used[l] = used[r] = 1;
                ans++, l++, r--;
            }
            else r--;
        }
        for(int i = 0; i < N; i++)
                ans += !used[i];
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
