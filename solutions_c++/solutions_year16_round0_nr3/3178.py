#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

namespace Primality {
    // 返回x与y相乘模m的结果，x与m要小于2^62
    LL MUL(LL x, LL y, LL m){
        LL c,s=0;
        for(c=x%m;y;c=(c+c)%m,y>>=1)
            if(y&1) s=(s+c)%m;
        return s;
    }
    // 返回x的y次方模m的结果，x与m要小于2^62
    LL POW(LL x, LL y, LL m){
        LL c,s=1;
        for(c=x%m;y;c=MUL(c,c,m),y>>=1)
            if(y&1) s=MUL(s,c,m);
        return s;
    }
    // 判断num是否为质数
    bool miller_rabin(LL num){
        if(num<=1) return false;
        if(num<=3) return true;
        if(~num&1) return false;
        const int u[]={2,3,5,7,11,13,17,19,23,29,0};
        LL e=num-1,a,c=0;
        while(~e&1) e/=2,c++;
        for(int i=0;u[i];i++){
            if(num<=u[i]) return true;
            a=POW(u[i],e,num);
            if(a==1) continue;
            for(int j=1;a!=num-1;j++){
                if(j==c) return false;
                a=MUL(a,a,num);
            }
        }
        return true;
    }
    // 求一个小于n的因数，期望复杂度为O(n^0.25)，当n为非合数时返回n本身
    LL pollard_rho(LL n){
        if(n<=3 || miller_rabin(n)) return n; // 保证n为合数时可去掉这行
        while(1){
            int i=1,cnt=2;
            LL x=rand()%n,y=x,c=rand()%n;
            if(!c || c==n-2) c++;
            do{
                LL u=__gcd(n-x+y,n);
                if(u>1 && u<n) return u;
                if(++i==cnt) y=x,cnt*=2;
                x=(c+MUL(x,x,n))%n;
            }while(x!=y);
        }
        return n;
    }
    // 使用rho方法对n做质因数分解，建议先筛去小质因数后再用此函数
    vector<LL> factorize(LL n){
        vector<LL> u;
        if(n>1) u.push_back(n);
        for(size_t i=0;i<u.size();i++){
            LL x=pollard_rho(u[i]);
            if(x==u[i]) continue;
            u[i--]/=x;
            u.push_back(x);
        }
        sort(u.begin(),u.end());
        return u;
    }
};

LL smallest_factor(LL n) {
    return Primality::pollard_rho(n);
}

bool check(int n, LL x) {
    vector<LL> v;
    for (int b = 2; b <= 10; ++b) {
        LL y = 0;
        for (int i = n-1; i >= 0; --i) {
            y = y * b + (x >> i & 1);
        }
        LL sf = smallest_factor(y);
        if (sf == y) return false;
        v.push_back(sf);
    }
    for (int b = 2; b <= 10; ++b) {
        LL y = 0;
        for (int i = n-1; i >= 0; --i) {
            y = y * b + (x >> i & 1);
        }
//        printf("base=%d, y=%lld\n", b, y);
    }
    for (int i = n-1; i >= 0; --i) {
        printf("%lld", x >> i & 1);
    }
    for (auto &f: v) printf(" %lld", f);
    puts("");
    return true;
}

void gao(int n, int m) {
    for (LL i = 1LL << (n-1) | 1, j = 0; j < m; i += 2) {
        if (check(n, i)) ++j;
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int n, j;
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", cas);
        gao(n, j);
    }
}
