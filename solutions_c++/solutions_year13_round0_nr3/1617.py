
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

long long palsquare[100];
bool isPalin(long long n){
    char num[20];
    sprintf(num, "%lld", n);
    int l = strlen(num);

    for(int i = 0; i < l/2; i++){
        if(num[i] != num[l-1-i])
            return false;
    }
    return true;
}

int main(){
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    int t, i, kase = 0, nPalSq = 0, cnt;
    long long a, b, n;

    for(n = 1; n <= 10000000; n++){
        if(isPalin(n) && isPalin(n*n)){
            palsquare[nPalSq++] = n*n;
        }
    }
    
    scanf("%d", &t);
    while(t--){
        scanf("%lld%lld", &a, &b);
        printf("Case #%d: ", ++kase);
        cnt = 0;
        for(int i = 0; i < nPalSq; i++){
            if(a <= palsquare[i] && palsquare[i] <= b)
                ++cnt;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
