# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Alargeout.txt", "w", stdout);
    long long n, i, m, ans;
    set <short> digits;
    int cases, caseno=0;
    scanf("%d", &cases);
    while(cases--){
        scanf("%lld", &n);
        if (n==0){
            printf("Case #%d: INSOMNIA\n", ++caseno);
            continue;
        }
        digits.clear();
        for (i=1; digits.size()<10; i++){
            m = n*i;
            ans = m;
            while(m){
                digits.insert(m%10);
                m/=10;
            }
        }
        printf("Case #%d: %lld\n", ++caseno, ans);
    }
    return 0;
}
