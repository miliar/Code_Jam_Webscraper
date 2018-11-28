#include <iostream>
#include <set>
#include <cstdlib>
#include <stdexcept>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const int IMPOSSIBLE=9999999;
int T,k,cas,ans,LEN;
char s[11111], sc[11111];

char oppo(char c){
    if (c=='+')
        return '-';
    if (c=='-')
        return '+';
    return '*';
}

int getans(){
    strcpy(sc, s);
    int cnt =0;
    for (int i=0; i<=LEN-k; i++){
        if (sc[i] == '-'){
            cnt++;
            for (int j=0; j<k; j++)
                sc[i+j] = oppo(sc[i+j]);
        }
    }
    for (int i=LEN-k+1; i<LEN; i++)
        if (sc[i]=='-')
            return IMPOSSIBLE;
    return cnt;
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.txt", "w", stdout);
    scanf("%d", &T);
    for (cas=1; cas<=T; cas++){
        scanf("%s %d", s, &k);
        LEN = strlen(s);

        ans = getans();

        for (int i=0; i+i<LEN-1; i++)
            swap(s[i], s[LEN-1-i]);

        ans = min(ans, getans());
        printf("Case #%d: ", cas);
        if (ans == IMPOSSIBLE)
            printf("IMPOSSIBLE");
        else
            printf("%d", ans);
        printf("\n");
    }
}
