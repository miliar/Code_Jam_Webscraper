#include <stdio.h>
#include <math.h>

using namespace std;

const int MAXN = 1e7;
typedef long long LL;
#define pb push_back

int t;

bool pal(LL x){
    int gx = x;
    LL y = 0;
    while (x){
        y *= 10;
        y += x % 10;
        x /= 10;
    }
    return gx == y;
}

int cs[MAXN + 1];

void foo(int is){
    LL l, r;
    scanf("%lld%lld", &l, &r);
    int L = (int)sqrt((double)l);
    int R = (int)sqrt((double)r);
    while ((LL)L * (LL)L < l)
    	L++;
    //printf("!%d %d", L, R);
    printf("Case #%d: %d\n", is, cs[R] - cs[L - 1]);


}


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);

    for (int i = 1; i <= MAXN; i++)
        cs[i] = pal((LL)i * (LL)i) && pal((LL)i) ? cs[i - 1] + 1 : cs[i - 1];
    

    for (int i = 0; i < t; i++)
        foo(i + 1);

    return 0;
}