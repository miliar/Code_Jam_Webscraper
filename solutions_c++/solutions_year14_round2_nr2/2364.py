#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int T, A, B, K, cnt;
    scanf("%d", &T);
    for(int i = 1; i <=T; i++){
        cnt = 0;
        scanf("%d %d %d", &A, &B, &K);
        for(int k = 0; k < A; k++)
            for(int j = 0; j < B; j++){
                if( (k & j) < K)
                    cnt++;
            }
        printf("Case #%d: %d\n", i, cnt);
    }
}
