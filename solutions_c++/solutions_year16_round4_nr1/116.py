#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int tc;
int n;
int r, p, s;
int ar[3], ap[3], as[3];
int cur;
char str[3][4100];

void f(int now, int s, int e){
    if(s == e){
        str[cur][s] = now;
        if(now == 'R') ar[cur]++;
        else if(now == 'P') ap[cur]++;
        else as[cur]++;
        return;
    }
    int m = (s + e) / 2;
    int a = now, b = (now == 'R') ? ('S') : (now == 'P') ? ('R') : ('P');
    f(a, s, m);
    f(b, m + 1, e);
    for(int i = s, j = m + 1; i <= m; i++, j++){
        if(str[cur][i] > str[cur][j]){
            rotate(str[cur] + s, str[cur] + m + 1, str[cur] + e + 1);
            break;
        }
    }
}

int main(){
    freopen("Al.in", "r", stdin);
    freopen("Al.out", "w", stdout);
    scanf("%d", &tc);
    for(int ttc = 1; ttc <= tc; ttc++){
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: ", ttc);
        for(int i = 0; i < 3; i++) ar[i] = ap[i] = as[i] = 0;
        cur = 0;
        f('R', 0, (1 << n) - 1);
        cur = 1;
        f('P', 0, (1 << n) - 1);
        cur = 2;
        f('S', 0, (1 << n) - 1);
        str[0][(1 << n)] = str[1][(1 << n)] = str[2][(1 << n)] = 0;
        if(r == ar[0] && p == ap[0] && s == as[0]){
            puts(str[0]);
        }
        else if(r == ar[1] && p == ap[1] && s == as[1]){
            puts(str[1]);
        }
        else if(r == ar[2] && p == ap[2] && s == as[2]){
            puts(str[2]);
        }
        else{
            puts("IMPOSSIBLE");
        }
    }
}
