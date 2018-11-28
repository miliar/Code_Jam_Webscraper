#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int N, J, counter;
int bit[40];

void rec(int len){
    if(counter == J)
        return;
    if(len == N){
        vector<long long> sol;
        for(int i = 2; i <= 10; ++i){
            long long cur = 0;
            long long mul = 1;
            for(int j = N; j >= 1; --j){
                cur+=bit[j]*mul;
                mul*=i;
            }
            bool isPrime = true;
            if(cur%2 == 0){
                sol.push_back(2);
                isPrime = false;
            }else{
                for(long long j = 3; j <= (long long)sqrt(cur); j+=2){
                    if(cur%j == 0){
                        sol.push_back(j);
                        isPrime = false;
                        break;
                    }
                }
            }
            if(isPrime)
                return;
        }
        counter++;
        for(int i = 1; i <= N; ++i)
            printf("%d", bit[i]);
        for(int i = 0; i < sol.size(); ++i)
            printf(" %lld", sol[i]);
        printf("\n");
        return;
    }
    bit[len] = 0;
    rec(len+1);
    bit[len] = 1;
    rec(len+1);
    return;
}
int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cases = 1; cases <= T; ++cases){
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", cases);
        bit[1] = 1;
        bit[N] = 1;
        rec(2);
    }
    return 0;
}
