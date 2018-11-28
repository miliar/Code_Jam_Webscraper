#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 10000+5;

int mp[5][5] = 
{
    0, 0, 0, 0, 0,
    0, 1, 2, 3, 4,
    0, 2, -1, 4, -3,
    0, 3, -4, -1, 2,
    0, 4, 3, -2, -1
};

int L, X;
char s[N];
int id[2222];

bool solve() {
    int pre = -1;
    int n = L*X;
    int cur = 0;
    for(int i = 0;i < n; i++) {
        if(i) {
            if(cur < 0) cur = -mp[-cur][id[s[i]]];
            else    cur = mp[cur][id[s[i]]];
        } else
            cur = id[s[i]];
        if(cur == 2 && pre == -1) pre = 0;
//        printf("i = %d cur = %d\n", i, cur);
        if(cur == 4 && pre != -1)   pre = 1;
    }
    if(pre == 1 && cur == -1)
        return true;
    return false;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    id['1'] = 1; id['i'] = 2;
    id['j'] = 3; id['k'] = 4;
    int t, cas = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &L, &X);
        scanf("%s", s);
        for(int i = 0;i < L*X; i++) if(i >= L)
            s[i] = s[i-L];
        printf("Case #%d: %s\n", cas++, solve()?"YES":"NO");
    }
    return 0;
}
