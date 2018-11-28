#include<bits/stdc++.h>
using namespace std;

int test;
long long longitud, multiplicaciones, gente;

int main(){
    freopen("D-small-attempt0.out", "w", stdout);
    freopen("D-small-attempt0.in", "r", stdin);
    ios::sync_with_stdio(false);
    scanf("%d", &test);
    for(int testCase = 1; testCase <= test; testCase++){
        scanf("%lld %lld %lld", &longitud, &multiplicaciones, &gente);
        if(longitud == gente){
            printf("Case #%d:", testCase);
            for(int i = 1; i <= gente; i++) printf(" %d", i);
            printf("\n");
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n", testCase);
        }
    }
    fclose(stdout);
}
