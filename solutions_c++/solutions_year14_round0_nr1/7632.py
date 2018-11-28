#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int f[20] ;

int main(){
    freopen("input.txt", "r", stdin) ;
    freopen("output.txt", "w", stdout) ;
    int T, cas = 1 ;
    scanf("%d", &T) ;
    while (T--){
        memset(f, 0, sizeof(f)) ;
        int cnt = 0;
        int ans ;
        for (int k = 0; k < 2; ++k){
            int r, x ;
            scanf("%d", &r) ;
            for (int i = 1; i <= 4; i++){
                for (int j = 1; j <= 4; j++){
                    scanf("%d", &x) ;
                    if (i == r && ++f[x] == 2){
                        cnt++ ;
                        ans = x ;
                    }
                }
            }
        }
        printf("Case #%d: ", cas++) ;
        if (cnt == 1){
            printf("%d\n", ans) ;
        }else   if (cnt == 0){
            printf("Volunteer cheated!\n") ;
        }else{
            printf("Bad magician!\n") ;
        }
    }
    return 0;
}
