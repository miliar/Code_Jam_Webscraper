#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#define ULL unsigned long long
#define LL long long
using namespace std;
LL prime[6] = {2, 3, 5, 233, 331};
LL qmul(LL x, LL y, LL mod) { // �˷���ֹ����� ���p * p����LL�Ļ�����ֱ�ӳˣ� O(1)�˷�����ת���ɶ����Ƽӷ�


    return (x * y - (long long)(x / (long double)mod * y + 1e-3) * mod + mod) % mod;
    /*
    LL ret = 0;
    while(y) {
        if(y & 1)
            ret = (ret + x) % mod;
        x = x * 2 % mod;
        y >>= 1;
    }
    return ret;
    */
}
LL qpow(LL a, LL n, LL mod) {
    LL ret = 1;
    while(n) {
        if(n & 1) ret = qmul(ret, a, mod);
        a = qmul(a, a, mod);
        n >>= 1;
    }
    return ret;
}
bool Miller_Rabin(LL p) {
    if(p < 2) return 0;
    if(p != 2 && p % 2 == 0) return 0;
    LL s = p - 1;
    while(!(s & 1)) s >>= 1;
    for(int i = 0; i < 5; ++i) {
        if(p == prime[i]) return 1;
        LL t = s, m = qpow(prime[i], s, p);
        while(t != p - 1 && m != 1 && m != p - 1) {
            m = qmul(m, m, p);
            t <<= 1;
        }
        if(m != p - 1 && !(t & 1)) return 0;
    }
    return 1;
}
int n, m;
LL k_base(int j,int k){
    LL cnt= 1,t = k;
    for(int i = 0; i < n-2; i++) {
        if(j & (1 << i)) cnt += t;
        t *= k;
    }
    cnt += t;
    return cnt;
}
vector<LL>ans;
int main() {
    freopen("data.in","r",stdin);
    freopen("check.out","w",stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while(T--) {

        scanf("%d %d", &n, &m);
        printf("Case #%d:\n",cas++);
        for(int j = 0; j < (1 << n-2); j++) {
            int ok=1;
            for(int k = 2; k <= 10; k++) {
                LL cnt=k_base(j,k);
                if(Miller_Rabin(cnt)){
                    ok=0;
                    break;
                }
            }
            if(ok) ans.push_back(j),m--;
            if(m==0) break;
        }
        for(int j=0;j<ans.size();j++){
            printf("1");
            for(int k=n-3;k>=0;k--){
                if(ans[j]&(1<<k)) printf("1");
                else printf("0");
            }
            printf("1");
            for(int k=2;k<=10;k++){
                LL cnt=k_base(ans[j],k);
                LL t=sqrt(cnt);
                for(int i=2;i<=t;i++){
                    if(cnt%i==0){
                        printf(" %d",i);
                        break;
                    }
                }
            }
            printf("\n");
        }
    }
    return 0;
}
