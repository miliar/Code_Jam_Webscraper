#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

long long n, sum;
int cnt, T;
bool h[10];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        memset(h, 0, sizeof(h));
        cnt = 0;
        sum = 0;
        scanf("%lld", &n);
        for (int i = 1; i < 2000000; ++ i){
            sum += n;
            long long tmp = sum;
            while (tmp > 0){
                if (!h[tmp % 10]){
                    cnt ++;
                    h[tmp % 10] = true;
                }
                tmp /= 10;
            }
            if (cnt == 10){
                printf("Case #%d: %lld\n", cas, sum);
                break;
            }
        }
        if (cnt != 10) printf("Case #%d: INSOMNIA\n", cas);
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
