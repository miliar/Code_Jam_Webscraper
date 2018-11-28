#include<cstdio>

int gcd(long long a, long long b){
    while((a%=b) && (b%=a));//printf("a=%lld, b=%lld\n", a, b);
    return a+b;
}

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--){
        long long num, den;
        scanf("%lld/%lld", &num, &den);
        int g = gcd(num, den);
//        printf("g=%d\n", g);
        num /= g;
        den /= g;
        bool possi = true;
        int ans = 0;
        while(den > 1 && possi){
//            printf("den=%lld\n", den);
            if(den % 2 != 0) possi = false;
            if((double)num/den < 1){
                ans++;
            }
            else break;
            den /= 2;
//            printf("%lf\n", (double)num/den);
        }
        printf("Case #%d: ", ++cnt);
        if(!possi) printf("impossible\n");
        else printf("%d\n", ans);
    }
    return 0;
}
