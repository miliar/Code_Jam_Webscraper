#include <stdio.h>
#include <memory.h>

typedef long long ll;
int test, n, cnt;
bool digit[10];

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int ii = 1; ii <= test; ++ii){
        scanf("%d", &n);
        if (n == 0){
            printf("Case #%d: INSOMNIA\n", ii);
            continue;
        }
        memset(digit, 0, sizeof(digit));
        cnt = 0;
        for (ll i = n;; i += n){
            ll j = i;
            while (j){
                if (digit[j % 10] == false)
                    ++cnt;
                digit[j % 10] = true;
                j /= 10;
            }
            if (cnt == 10){
                printf("Case #%d: %lld\n", ii, i);
                break;
            }
        }
    }
    return 0;
}
