#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
typedef long long LL;
LL n , ans;
bool mark[11];
void change(LL t) {
    while(t) {
        LL tmp = (t % (LL)10);
        mark[tmp] = 1;
        t /= 10;
    }
}
int main() {
    int T , cas = 1;
    freopen("A-large (1).in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> T;
    while(T--) {
        memset(mark, 0, sizeof(mark));
        scanf("%I64d", &n);
        LL cnt = 1; LL ans = 0; LL num;
        while(1) {
            num = cnt * n; cnt++;
            change(num);
            ans++;
            bool flag = 1;
            for(int i=0; i<=9; ++i) {
                if(!mark[i]) {
                    flag = 0;
                }
            }
            if(ans >= 6000000) break;
            if(flag) break;
        }
        printf("Case #%d: ", cas++);
        if(ans >= 6000000) printf("INSOMNIA\n");
        else cout << num << endl;
    }
    return 0;
}
