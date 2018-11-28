#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int n, t, cases;
#define S 205
char ch[S];
int main(){
    freopen("b_large.in", "r", stdin);
    freopen("b_large.out", "w", stdout);
    scanf("%d", &t);
    while(t--){
        scanf("%s", ch);
        int len = strlen(ch);
        int ans = 0;
        for(int i = len - 1; i >= 0; --i){
            int face = (ch[i] == '+' ? 1 : 0);
            if((face && (ans % 2)) || (!face && (ans % 2 == 0)) ){
                ans++;
            }
        }
        printf("Case #%d: %d\n", ++cases, ans);
    }
    return 0;
}
