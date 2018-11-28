#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

typedef pair<int, int> PII;
typedef pair<pair<int, int>, int> triple;
typedef map<string, int> MSI;
typedef map<string, char> MSC;
typedef map<int, int> MII;
typedef map<char, int> MCI;
typedef map<PII, int> MPI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define zero(a) memset(a, 0, sizeof(a))
#define MP make_pair
#define PB push_back
#define F first
#define S second
//-----------------------------
#define MAXN 1000
#define MAXM 1000
#define MOD 1000000007

int T;
int n;
bool use[10];

int main() {
    // freopen("A-large.in", "r", stdin);
    // freopen("output_big.txt", "w", stdout);

    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%d", &n);
        if (n  == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }

        int n_base = 0;
        int now_n = n;
        zero(use);
        int now = 0;

        while (now < 10) {
            ++n_base;
            now_n = n_base * n;
            while (now_n) {
                if (!use[now_n % 10]) {
                    ++now;
                    use[now_n % 10] = true;
                }
                now_n /= 10;
            }
            if (now == 10) {
                printf("Case #%d: %d\n", i, n_base * n);
                continue;
            }
        }
    }
    return 0;
}
