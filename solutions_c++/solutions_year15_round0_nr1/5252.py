#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

const int N = 1010;

int Smax, Ans, Stand, New;
char S[N];

int main(){
    //freopen("A.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0; scanf("%d", &T);
    while (T--){
        scanf("%d %s", &Smax, S);

        Ans = 0; Stand = S[0] - '0';
        for(int i = 1; i <= Smax; i ++){
            if (S[i] == '0') continue;
            if (Stand < i) New = i - Stand;
            Ans += New;
            Stand += New + S[i] - '0';
            New = 0;
        }
        printf("Case #%d: %d\n", ++cas, Ans);
    }
}
