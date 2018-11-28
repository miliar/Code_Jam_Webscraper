#include <bits/stdc++.h>
using namespace std;
int n, tab[1007],t;
int upper(int x, int y){
    return (x + y-1)/y;
}
int main(){
    scanf("%d",&t);
    for(int k = 0; k < t; k++){
        printf("Case #%d: ", k+1);
        scanf("%d",&n);
        for(int i = 0; i < n; i++)
            scanf("%d",&tab[i]);
        int best = 1000007;
        for(int p = 1; p < 1007; p++){
            int cost = 0;
            for(int i = 0; i < n; i++){
                cost += (tab[i] - 1) / p;
            }
            best = min(best, cost + p);
        }
        printf("%d\n", best);
    }
}
