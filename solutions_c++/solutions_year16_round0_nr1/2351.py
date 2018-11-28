#include <cstdio>
#include <cstring>
typedef long long LL;
bool HashTable[20];
int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int T, tcase = 1;
    scanf("%d", &T);
    while(T--) {
        LL n;
        scanf("%lld", &n);
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", tcase++);
            continue;
        }
        memset(HashTable, false, sizeof(HashTable));
        for(LL i = 1; ; i++) {
            LL temp = n * i;
            while(temp) {
                HashTable[temp % 10] = true;
                temp /= 10;
            }
            bool flag = true;
            for(int j = 0; j <= 9; j++) {
                flag &= HashTable[j];
            }
            if(flag) {
                printf("Case #%d: %lld\n", tcase++, n * i);
                break;
            }
        }
    }
    return 0;
}
