#include <cstdio>
#include <cstring>
typedef long long ll;
int kase, n, J;
ll low, divisor[9];
ll change(ll num, int base) {
    if (base==2)
        return num;
    ll res=0;
    int digit=n-1;
    while (digit>=0) {
        if (num&(1<<digit)) {
            res++;
        }
        res*=base;
        digit--;
    }
    res/=base;
    return res;
}
void print(int num) {
    printf("%lld", change(num, 10));
    for (int i=0; i<9; i++)
        printf(" %lld", divisor[i]);
    puts("");
}
bool judge(ll num, int ind) {
    for (ll i=2; i*i<=num; i++)
        if (num%i==0) {
            divisor[ind]=i;
            return true;
        }
    return false;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        printf("Case #%d:\n", cas);
        scanf("%d%d", &n, &J);
        int cnt=0;
        low=(1<<(n-1))+1;
        for (ll i=low; cnt<J; i+=2) {
            memset(divisor, 0, sizeof(divisor));
            ll temp;
            bool flag=false;
            for (int j=2; j<=10; j++) {
                temp=change(i, j);
                if (!judge(temp, j-2)) {
                    flag=true;
                    break;
                }
            }
            if (!flag) {
                print(i);
                cnt++;
            }
        }
    }
    return 0;
}
