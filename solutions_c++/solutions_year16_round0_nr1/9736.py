#include <set>
#include <stdio.h>

using namespace std;

#define FIN freopen("A-large.in", "r", stdin)
#define FOUT freopen("A-large.out", "w", stdout)

bool check(set<int> &s, int x) {
    while(x != 0) {
        int d = x % 10;
        s.insert(d);
        x /= 10;
    }
    return s.size() == 10;
}

int bfs(int base) {
    int n = base;
    set<int> s;
    int ret = -1;
    while(true) {
        if(check(s, n)) {
            ret = n;
            break;
        }
        n += base;
    }
    return ret;
}

int main() {
    FIN;
    FOUT;
    int T, n, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &n);
        printf("Case #%d: ", ++ncase);
        if(n == 0) {
            printf("%s\n", "INSOMNIA");
        }
        else {
            int ans = bfs(n);
            printf("%d\n", ans);
        }
    }
    return 0;
}
