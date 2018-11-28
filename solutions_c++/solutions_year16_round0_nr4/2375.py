# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("Dsmallout.txt", "w", stdout);
    int cases, caseno=0, k, c, s;
    scanf("%d", &cases);
    while(cases--){
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d:", ++caseno);
        for (int i=1; i<=s; i++) printf(" %d", i);
        printf("\n");
    }
    return 0;
}
