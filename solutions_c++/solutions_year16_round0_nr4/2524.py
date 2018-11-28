#include <bits/stdc++.h>
using namespace std;
int main(){
    int T, cases=1;
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", cases++);
        for(int i=1;i<=k;i++)printf(" %d", i);
        printf("\n");
    }
    return 0;
}
