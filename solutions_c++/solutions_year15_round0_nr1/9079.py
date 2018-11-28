#include <stdio.h>
#include <stdlib.h>

int main(){
    int times;
    scanf("%d", &times);
    for(int i = 0; i < times; ++i){
        int T;
        int *arr;
        scanf("%d", &T);
        arr = (int *)malloc(sizeof(int) * (T+1));

        for(int j = 0; j <= T; ++j){
            scanf("%1d", &arr[j]);
        }

        int cnt = 0, ans = 0;

        for(int j = 0; j <= T; ++j){
            if(arr[j] == 0 && cnt < j+1){
                arr[j] = 1;
                ans++;
            }
            if(cnt < j){
                arr[j] = 1;
                ans += arr[j];
            }
            cnt += arr[j];
            //printf("%d %d %d\n", j, arr[j], cnt);
        }
        printf("Case #%d: %d\n", i+1, ans);

        free(arr);
    }
    return 0;
}
