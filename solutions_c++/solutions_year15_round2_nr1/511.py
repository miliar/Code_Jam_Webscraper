#include <bits/stdc++.h>
#define snuke(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define out(x) std::cout<<(#x)<<":"<<(x)<<std::endl
#define ALL(v) (v).begin(), (v).end()
#define SZ(v) ((int)(v).size())
template<class T> void Read(T&ret){ret=0;bool ok=0,u=0;for(;;){int c=getchar();if(c>='0'&&c<='9')ret=(ret<<3)+(ret<<1)+c-'0',ok=1;else if(c=='-')u=1;else if(ok){if(u)ret*=-1;return;}}}
long long pow_mod(long long p,int n,long long mod){long long ret=1;for(;n;n>>=1){if(n&1)ret=ret*p%mod;p=p*p%mod;}return ret;}
template <class T> bool chmin(T& a, const T &b) {return b < a? a = b, 1: 0;}
template <class T> bool chmax(T& a, const T &b) {return b > a? a = b, 1: 0;}
/****head****/
int _;
long long XT;
long long ten[111];
int stk[111], stk_top;
int reverse(long long n) {
        int &r = stk_top; r = 0;
        while(n) {
                stk[r++] = n % 10;
                n /= 10;
        }
        long long ret = 0;
        for(int i = 0; i < r; ++i) {
                ret = ret * 10 + stk[i];
        }
        return ret;
}
long long calc(long long t) {
        long long ret = 0;
        while(t % 10 == 0) {
                --t; ++ret;
        }

        long long up = 1;
        while(up * 10 <= t) up *= 10;
        if(up > 1) {
                for(long long i = 1, len = 1; i < up; i *= 10, ++len) {
                        int l = len >> 1;
                        ret += ten[len-l] + ten[l] - 1;
                }
        } else {
                ++ret;
        }

        long long ret2 = ret + t - up;
        
        reverse(t);
        int r = stk_top;
        long long tmp = 0;
        for(int i = (r+1) >> 1; i < r; ++i) {
                tmp = tmp * 10 + stk[i];
        }
        ret += tmp + 1;
        tmp = 0;
        for(int i = ((r + 1) >> 1) - 1; i >= 0; --i) {
                tmp = tmp * 10 + stk[i];
        }
        ret += tmp - 1;
        chmin(ret, ret2);
        return ret;
}
int main() {
        //freopen("tst.in","r",stdin);
        freopen("my.out","w",stdout);
        ten[0] = 1;
        for(int i = 1; i <= 16; ++i) ten[i] = ten[i-1] * 10ll;

        for(scanf("%d", &_); _--; ) {
                long long n; scanf("%I64d", &n);
                XT = n;
                static int cas = 0;
                long long ans = calc(n);
                printf("Case #%d: %I64d\n", ++cas, ans);
        }
        return 0;
}
