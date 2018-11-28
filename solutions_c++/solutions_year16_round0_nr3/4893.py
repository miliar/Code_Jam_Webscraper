#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 1000;
const long long INF = 1e9 + 19;

int n, k;

int a[N];
int b[N];

int isPrime(long long x) {
    for (int i = 2; i < 1000 && i < x; i++)
        if (x % i == 0)
            return i;
    return -1;
}

set < int > q;

void read() {
    scanf("%d%d", &n, &k);
    for (int tt = 0; tt < k; tt++) {
        for (int iter = 0; ; iter++) {
            for (;;) {
                for (int i = 0; i < n; i++)
                    a[i] = rand() % 2;    
                a[0] = 1; 
                a[n - 1] = 1;
                int x = 0;
                for (int i = 0; i < n; i++)
                    x = x * 2 + a[i];
                if (q.count(x) == 0) {
                    q.insert(x);
                    break;
                }
            }
            bool flag = 1;
            for (int base = 2; base <= 10; base++) {
                long long x = 0;
                for (int i = 0; i < n; i++)
                    x = x * base + a[i];
                b[base] = isPrime(x);
                if (b[base] == -1) {
                    flag = 0;
                    break;
                }
            }
            //if (flag == 0)
                //cerr << "fail\n";
            if (flag) {
                for (int i = 0; i < n; i++)
                    printf("%d", a[i]);
                for (int base = 2; base <= 10; base++)
                    printf(" %d", b[base]);
                puts("");
                break;
            }
        }



    } 

}

void solve() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: \n", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}

