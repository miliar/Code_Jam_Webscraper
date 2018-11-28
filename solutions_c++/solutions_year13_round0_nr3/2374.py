#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 105;
const int INF = 1 << 29;
const long long MOD = 55566677ll;
const int dx[] = {-1, 0, 0, 1, 1, 1, -1, -1};
const int dy[] = {0, -1, 1, 0, 1, -1, -1, 1};

long long a, b;
long long f[255];
int tot;

char s[100];
inline bool check(long long x){
    sprintf(s, "%lld", x);
    int l = strlen(s);
    for (int i = 0;i < l / 2;i++){
        if (s[i] != s[l - i - 1]) return false;
    }
    return true;
}

void prep(){
    tot = 0;
    for (long long i = 1;i * i <= 1000000000000000ll;i++){
//        printf("%lld\n", i);
        if (check(i) && check(i * i)){
            f[tot] = i * i;
            tot += 1;
//            printf("%lld %lld\n", i, i * i);
        }
    }
//    printf("tot %d\n", tot);
}

void init(){
    if (scanf("%lld%lld", &a, &b) == EOF) exit(0);
//    printf("%lld %lld\n",a , b);
}

inline int gao(long long x){
    for (int i = 0;i < tot;i++){
        if (f[i] > x){
            return i;
        }
    }
}

void work(){
//    gao(b);
    printf("%d\n", gao(b) - gao(a - 1));
}

int main(){
#ifdef LATTE
//    freopen("c.in", "r", stdin);
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
#endif
    int T, t = 0;
    prep();
    scanf("%d", &T);
    while (T--){
        init();
        printf("Case #%d: ", ++t);
        work();
    }
    return 0;
}
