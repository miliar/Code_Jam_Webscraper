#include<bits/stdc++.h>
using namespace std;

int test, cont, decimal;
long long n, num;
bool si[10];

inline void check(long long numero){
    while(numero > 0){
        decimal = numero % 10;
        numero /= 10;
        if(!si[decimal]){
            si[decimal] = true;
            cont++;
        }
    }
}

inline void solve(int testCase){
    if(n == 0){
        printf("Case #%d: INSOMNIA\n", testCase);
        return;
    }

    for(int i = 0; i < 10; i++) si[i] = false;
    cont = 0;
    num = n;

    while(true){
        check(num);
        if(cont == 10){
            printf("Case #%d: %d\n", testCase, num);
            break;
        }
        num += n;
    }
}

int main(){
    freopen("A-large.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    ios::sync_with_stdio(false);
    scanf("%d", &test);
    for(int testCase = 1; testCase <= test; testCase++){
        scanf("%lld", &n);
        solve(testCase);

    }
    fclose(stdout);
}
