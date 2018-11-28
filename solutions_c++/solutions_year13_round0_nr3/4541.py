#include <cstdio>
#include <set>
using namespace std;

int t;
int a, b;
set <long long> ps;

bool pldr(long long pl){
    char d[20] = {0};
    int len = 0;
    while(pl){
        d[len ++] = pl % 10;
        pl /= 10;
    }
    for(int i = 0; i < len / 2; i ++)
        if(d[i] != d[len - i - 1])
            return false;
    return true;
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &t);
    for(int i = 1; i < 10000000; i ++){
        if(pldr(i)){
            long long sq = i * 1ll * i;
            if(pldr(sq))
                ps.insert(sq);
        }
    }
    for(int c = 1; c <= t; c ++){
        scanf("%d%d", &a, &b);
        int cnt = 0;
        for(set <long long> :: iterator it = ps.begin(); it != ps.end(); it ++)
            if((a <= *it) && (*it <= b))
                cnt ++;
        printf("Case #%d: %d\n", c, cnt);
    }
    fflush(stdout);
    return 0;
}
