#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int N, J, cnt = 0;
int str[35];

void rec(int len){
    if(cnt == J)
        return;
    if(len == N){
        /*
        printf("->");
        for(int i = 1; i <= N; ++i)
            printf("%d", str[i]);
        printf("\n");
        //*/
        vector<long long> ans;
        for(int i = 2; i <= 10; ++i){
            long long now = 0, mul = 1;
            for(int j = N; j >= 1; --j){
                now+=str[j]*mul;
                mul*=i;
            }
            //printf("%d: %d\n", i, now);
            bool isPrime = true;
            if(now%2 == 0){
                ans.push_back(2);
                isPrime = false;
            }
            else{
                for(long long j = 3; j <= (long long)sqrt(now); j+=2){
                    if(now%j == 0){
                        ans.push_back(j);
                        isPrime = false;
                        break;
                    }
                }
            }
            if(isPrime)
                return;
        }
        cnt++;
        for(int i = 1; i <= N; ++i)
            printf("%d", str[i]);
        for(int i = 0; i < ans.size(); ++i)
            printf(" %lld", ans[i]);
        printf("\n");
        return;
    }
    str[len] = 0;
    rec(len+1);
    str[len] = 1;
    rec(len+1);
    return;
}

int main(){
    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for(int cases = 1; cases <= totalCase; ++cases){
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", cases);
        str[1] = str[N] = 1;
        rec(2);
    }
    return 0;
}
/*
1
6 3
*/
