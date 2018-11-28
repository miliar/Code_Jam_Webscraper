#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using namespace std;

#define MAX 1005
int N, J;
bool work[MAX];
vector <int> primes, dv[9];
vector <long long> ans;

void seive() {
    for(int i = 2; i < MAX; i++) {
        if(work[i]) continue;
        primes.push_back(i);
        for(int j = i; j < MAX; j += i) work[j] = true;
    }
}

int bigmod(int a, int pow, int md) {
    int ret = 1;
    while(pow > 0) {
        if(pow & 1) ret = (ret * a) % md;
        pow >>= 1;
        a = (a * a) % md;
    }
    return ret;
}

void print(long long msk) {
    for(int i = N-1; i >= 0; i--) {
        if(msk & (1LL << i)) putchar('1');
        else putchar('0');
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    seive();
    int t, ca = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d %d", &N, &J);
        long long mx = (1LL << N);
        long long msk = 1 | (1LL << (N-1));
        while(msk < mx && ans.size() < J) {
            int fl[11];
            bool pos = true;
            memset(fl, -1, sizeof(fl));

            for(int p = 0; p < primes.size(); p++) {
                for(int b = 2; b <= 10; b++) if(fl[b] == -1) {
                    int rem = 0;
                    for(int i = 0; i < N; i++) if(msk & (1LL << i))
                        rem = (rem + bigmod(b, i, primes[p])) % primes[p];
                    if(!rem) fl[b] = primes[p];
                }
            }
            for(int b = 2; b <= 10; b++) if(fl[b] == -1) pos = false;
            if(pos) {
                ans.push_back(msk);
                for(int b = 2; b <= 10; b++) dv[b-2].push_back(fl[b]);
            }
            msk += 2;
        }

        printf("Case #%d:\n", ca++);
        for(int i = 0; i < J; i++) {
            print(ans[i]);
            for(int j = 0; j <= 8; j++) printf(" %d", dv[j][i]);
            puts("");
        }
    }
}
