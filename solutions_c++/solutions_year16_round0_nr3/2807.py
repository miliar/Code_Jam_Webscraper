#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <string>
#include <time.h>
#define clr(x,c) memset(x, c, sizeof(x))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define psi pair<string, int>
#define LLD_MAX 9223372036854775807LL
#define LLD_MIN (-LLD_MAX - 1LL)
#define inf 0x3f3f3f3f
typedef long long lld;
typedef unsigned long long ulld;
using namespace std;

const int MAXNP = 11111;

bool vis[MAXNP];
vector<int> primes;

void findPrimes(const int N)
{
    clr(vis, 0);
    for (int x = 2; x < N; ++x) {
        if (!vis[x]) primes.pb(x);
        for (int j = 0; x * primes[j] < N; j++) {
            vis[x * primes[j]] = 1;
            if (x % primes[j] == 0) break;
        }
    }
}

lld getNum(int x, int b)
{
    lld ret = 0, top = 1;
    for (int i = 0; i <= 15; ++i) {
        ret = top * (x & 1) + ret;
        top *= b;
        x >>= 1;
    }
    return ret;
}

int check(const lld num)
{
    for (int p : primes) {
        if (num % p == 0) return p;
    }
    return 0;
}

int main ()
{
//    freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
//    freopen("C:/Users/ywy/Desktop/in.txt", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
    findPrimes(MAXNP);
//    cout << primes.size() << endl;
    int t, cas = 1;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        printf("Case #%d:\n", cas++);
        int s = (1 << (n-1)) | 1, e = (1 << n) - 1;
        for (int x = s, b; x <= e; x += 2) {
            vector<int> tmp;
            for (b = 2; b <= 10; ++b) {
                lld num = getNum(x, b);
                int p = check(num);
                if (!p) break;
                tmp.pb(p);
            }
            if (b > 10) {
                bool flag = false;
                for (int i = n-1; i >= 0; --i) {
                    printf("%d", (x & (1 << i)) >> i);
                }
                for (int p : tmp) {
                    printf(" %d", p);
                }
                printf("\n");
//                for (b = 2; b <= 10; ++b) {
//                    lld num = getNum(x, b);
//                    if (num % tmp[b-2] != 0) {
//                        cout << "!!!!!!!!!!" << endl;
//                    } else {
//                        cout << "(" << b << ": " << num << " " << tmp[b-2] << ") ";
//                    }
//                }
//                cout << endl;
                if (--m == 0) break;
            }
        }
    }
    return 0;
}

