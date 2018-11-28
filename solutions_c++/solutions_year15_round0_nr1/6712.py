#include <iostream>
#include <cstdio>
using namespace std;
#define forn(i, n) for(int i = 0; i < (n); i++)

int maxS, TC, ans;
string code;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc; scanf("%d", &tc);
    while(tc--){
        scanf("%d", &maxS);
        cin >> code;
        int parados = 0;
        ans = 0;
        forn(i, code.size()){
            if(parados >= i || code[i] == '0'){ // si ya se paró la gente que se necesita
                parados += code[i] - '0';
            }
            else {
                int aux = i - parados;
                parados += aux;
                parados += code[i] - '0';
                ans += aux;
            }
        }
        printf("Case #%d: %d\n", ++TC, ans);
    }
    return 0;
}
