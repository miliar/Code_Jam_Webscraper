#include<bits/stdc++.h>
using namespace std;

int test, length, options, cont;
long long posi, limit, arr[11], num, mult, divisor, raiz, divide, elNum[11];
bool si;

inline void divi(){
    divisor = -1;
    if((num & 1) == 0){
        divisor = 2;
    }
    else{
        raiz = sqrt(num);
        for(divide = 3; divide <= raiz; divide += 2)
            if(num % divide == 0){
                divisor = divide;
                break;
            }
    }
}

inline void solve(){
    limit = 1 << length;
    posi = (1 << (length - 1)) + 1;
    cont = 0;
    while(cont < options){
        si = true;
        for(int i = 2; i < 11; i++){
            num = 0;
            mult = 1;
            for(int bit = 0; bit < length; bit++, mult *= i)
                if((1 << bit) & posi){
                    num += mult;
                }
            divi();
            if(divisor == -1){
                si = false;
                break;
            }
            else{
                arr[i] = divisor;
                //elNum[i] = num;
            }
        }
        if(si){
            for(int bit = length - 1; bit > -1; bit--)
                if((1 << bit) & posi){
                    printf("1");
                }
                else{
                    printf("0");
                }
            for(int i = 2; i < 11; i++) printf(" %lld", arr[i]);
           // for(int i = 2; i < 11; i++) printf(" (%lld = %lld)", elNum[i], arr[i]);
            printf("\n");
            cont++;
        }
        posi += 2;
    }
}

int main(){
    freopen("C-small-attempt0.out", "w", stdout);
    freopen("C-small-attempt0.in", "r", stdin);
    ios::sync_with_stdio(false);
    scanf("%d", &test);
    for(int testCase = 1; testCase <= test; testCase++){
        scanf("%d %d", &length, &options);
        printf("Case #%d:\n", testCase);
        solve();
    }
    fclose(stdout);
}
