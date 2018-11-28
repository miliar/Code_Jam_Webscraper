#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<set>
#include<stack>
#include<cmath>
#include<climits>
using namespace std;
set<__uint128_t> s;

long long rec[100];

__uint128_t _pick(int x){
    __uint128_t now = -1LL;
    while(now == -1 || s.find(now) != s.end()){
        now = 1LL;
        for(int i = 0 ; i < x-2 ; i++){
            now = (now << 1) + rand() % 2;
        }
        now = (now << 1) + 1;
    }
    return now;
}

__uint128_t pick(int x){
    __uint128_t ans = -1;
    while(ans == -1){
        __uint128_t tmp = _pick(x);
        bool flag = true;
        for(int i = 2 ; i <= 10 ; i++){
            __uint128_t base = 1;
            __uint128_t t = tmp, num =0;
            while(t){
                if(t&1) num += base;
                t >>= 1;
                base *= i;
            }
            flag = false;
            for(long long j = 2 ; /* (__uint128_t)j*j <= sqrt(num) */ j <= 10000 ; j++){
                if(num % j == 0){
                    rec[i] = j;
                    flag = true;
                    break;
                }
            }
            if(flag == false) break;
        }
        if(flag) ans = tmp;
    }
    return ans;
}

int main(){
    srand(time(0));
    int TN;
    int n, m;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d:\n", casen);
        scanf("%d %d", &n, &m);
        while(m--){
            __uint128_t tmp = pick(n);
            stack<int> s;
            while(tmp){
                s.push(tmp & 1);
                tmp >>= 1;
            }
            while(!s.empty()){
                putchar(s.top() + '0');
                s.pop();
            }
            for(int i = 2 ; i <= 10 ; i++)
                printf(" %lld", rec[i]);
            puts("");
        }
    }
    return 0;
}
