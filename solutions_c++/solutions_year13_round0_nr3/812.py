#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

vector<long long> res;

bool check(long long n) {
    char buffer[32];
    sprintf(buffer, "%lld", n);
    int len = strlen(buffer);
    for (int i = 0; i < len / 2; ++ i) {
        if (buffer[i] != buffer[len-1-i]) {
            return false;
        }
    }
    return true;
}

int main () {
    for (long long k = 1; k <= 10000000; ++ k) {
        long long square = k * k;
        if (check(k) && check(square)) {
            res.push_back(square);
            //printf("%lld\n", square);
        }
    }
    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ++ ti) {
        long long A, B;
        scanf("%lld%lld", &A, &B);
        int cnt = 0;
        for (int i = 0; i < res.size(); ++ i) {
            if (res[i] >= A && res[i] <= B) {
                ++ cnt;
            }
        }
        printf("Case #%d: %d\n", ti, cnt);
    }
}
