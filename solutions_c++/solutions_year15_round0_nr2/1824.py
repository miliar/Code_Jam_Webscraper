#include<cstdio>
#include<algorithm>
using namespace std;

int arr[1002];

int main(){
    int tc;
    scanf("%d", &tc);
    for(int T = 1; T <= tc; ++T){
        int n, mx = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; ++i){
            scanf("%d", arr+i);
            mx = max(mx, arr[i]);
        }
        int result = 1000000000;
        for (int i = 1; i <= mx; ++i){
            int cnt = i;
            for (int j = 0; j < n; ++j){
                if(arr[j] > i)
                    cnt += ( arr[j] / i ) - (arr[j] % i == 0 );
            }
            //fprintf(stderr, "%d\n", cnt);
            result = min(result, cnt);
        }
        printf("Case #%d: %d\n", T, result);
    }
    return 0;
}

