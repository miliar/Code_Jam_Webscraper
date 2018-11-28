#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char s[15] ;
int n , ans ;

int main(){
    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;
    int _ , cas = 0 ; scanf("%d",&_) ;
    while (_--){
        scanf("%d%s" , &n , s) ;
        //cout << n << " " << s << endl ;
        int already = 0 , need = 0 ;
        for (int i = 0 ; i <= n ; i++){
            if (already < i){
                need += i - already ;
                already += i - already ;
            }
            already += s[i] - '0' ;
        }
        printf("Case #%d: %d\n",++cas , need) ;
    }
    return 0 ;
}
