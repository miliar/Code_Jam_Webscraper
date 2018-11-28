#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

char str[100005];

int get_num(int ch) {
    if (ch == 'i') return 0;
    if (ch == 'j') return 1;
    if (ch == 'k') return 2;
}

int get_char(int x) {
    if (x == 0) return 'i';
    if (x == 1) return 'j';
    if (x == 2) return 'k';
}

pair<int, int> multi(pair<int, int> a, pair<int, int> b) {
    if (a.first == 1) return make_pair(b.first, a.second * b.second);
    if (b.first == 1) return make_pair(a.first, a.second * b.second);
    int ne = a.second * b.second;
    int x = get_num(a.first), y = get_num(b.first);
    if ((x + 1) % 3 == y) return make_pair(get_char((y + 1) % 3), ne);
    if ((y + 1) % 3 == x) return make_pair(get_char((x + 1) % 3), -ne);
    return make_pair(1, -ne);
}

int L;
LL X;

int check() {
    pair<int, int> P;
    int t = X * L;
    for (int i = L; i < t; ++i)
        str[i] = str[i - L];
    P = make_pair(1, 1);
    int flag1 = -1, flag2 = -1, ne = 1;
    for (int i = 0; i < t; ++i) {
        P = multi(P, make_pair(str[i], 1));
        if (P.first == (int)'i') {
            flag1 = i;
            ne *= P.second;
            break;
        }
    }
    P = make_pair(1, 1);
    for (int i = t - 1; i >= 0; --i) {
        P = multi(make_pair(str[i], 1), P);
        if (P.first == (int)'k') {
            flag2 = i;
            ne *= P.second;
            break;
        }
    }
    if (flag1 == -1 || flag2 == -1 || flag1 >= flag2)
        return 0;
    P = make_pair(1, 1);
    for (int i = flag1 + 1; i < flag2; ++i) {
        P = multi(P, make_pair(str[i], 1));
    }
    if (P.first == (int)'j' && P.second * ne == 1) return 1;
    return 0;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, tcase = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%lld", &L, &X);
        scanf("%s", str);
        printf("Case #%d: ", ++tcase);
        if (check()) puts("YES");
        else puts("NO");
    }
    return 0;
}
