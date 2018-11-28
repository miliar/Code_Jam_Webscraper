#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<ctime>
#include<queue>
#include<utility>
#include<climits>

using namespace std;

#define mcpy(from, to) memcpy((to),(from),sizeof((from)))
#define msetz(pp) memset((pp),0,sizeof((pp)))
#define mseto(pp) memset((pp),1,sizeof((pp)))
#define msetno(pp) memset((pp),-1,sizeof((pp)))
#define mseti(pp) memset((pp),0x3f3f3f3f,sizeof((pp)))
#define msetni(pp) memset((pp),0xc0c0c0c0,sizeof((pp)))
typedef pair<int, int> PII;
//typedef __int64 LL;
typedef long long LL;
const int INF = 0x3f3f3f3f;
const LL LINF = 1ll << 60;
const double inf = 1e20, eps = 1e-8;

int ceil(int aa, int bb) {
    if (bb < 0) {
        aa = -aa;
        bb = -bb;
    }
    if (aa > 0) return (aa - 1) / bb + 1;
    else return aa / bb;
}

int floor(int aa, int bb) {
    if (bb < 0) {
        aa = -aa;
        bb = -bb;
    }
    if (aa >= 0) return aa / bb;
    else return (aa + 1) / bb - 1;
}

void readint(int &x) {
    char c;
    while (c = getchar(), (c < '0' || c > '9') && (c != '-'));
    bool flag = (c == '-');
    if (flag) c = getchar();
    x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + c - 48;
        c = getchar();
    }
    if (flag) x = -x;
}

void readLL(LL &x) {
    char c;
    while (c = getchar(), (c < '0' || c > '9') && (c != '-'));
    bool flag = (c == '-');
    if (flag) c = getchar();
    x = 0ll;
    while (c >= '0' && c <= '9') {
        x = x * 10ll + LL(c - 48);
        c = getchar();
    }
    if (flag) x = -x;
}

void putint(int x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    int len = 0, data[10];
    while (x) {
        data[len++] = x % 10;
        x /= 10;
    }
    if (!len) data[len++] = 0;
    while (len--) putchar(data[len] + 48);
    putchar('\n');
}

void putLL(LL x) {
    if (x < 0ll) {
        putchar('-');
        x = -x;
    }
    int len = 0, data[30];
    while (x > 0ll) {
        data[len++] = x % 10ll;
        x /= 10ll;
    }
    if (!len) data[len++] = 0;
    while (len--) putchar(data[len] + 48);
    putchar('\n');
}

#include<deque>
const int MAXN = 1005;

char str[MAXN];

int main() {
    int TT;
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    readint(TT);
    for (int TTT = 1; TTT <= TT; TTT++) {
        scanf("%s", str);
        printf("Case #%d: ", TTT);
        deque<char> qq;
        int ls = strlen(str);
        for (int i = 0; i < ls; i++) {
            if (qq.size() == 0 || str[i] >= qq.front()) qq.push_front(str[i]);
            else qq.push_back(str[i]);
        }
        for (auto cc : qq) {
            printf("%c", cc);
        }
        puts("");
    }
    return 0;
}