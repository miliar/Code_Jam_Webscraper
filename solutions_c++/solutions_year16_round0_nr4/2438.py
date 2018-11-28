#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int T, K, C, S;
unsigned long long* sol;

int main(){
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t){
        printf("Case #%d: ", t);
        scanf("%d %d %d\n", &K, &C, &S);
        sol = new unsigned long long [K];
        for (int i = 1; i <= K; ++i){
            sol[i-1] = i;
        }
        for (int i = 1; i < C; ++i){
            for (int j = 1; j <= K; ++j){
                sol[j-1] = (sol[j-1]-1) * K + j;
            }
        }
        for (int i = 0; i < K; ++i){
            printf("%lld", sol[i]);
            if (i != K-1) printf(" ");
            else printf("\n");
        }
        delete [] sol;
    }
}
