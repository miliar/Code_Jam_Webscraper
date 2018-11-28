
#include <cstdio>
#include <cstring>

int main()
{
    int T ;
    scanf("%d", &T) ;
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ; 
        int sm ; 
        scanf("%d", &sm) ;
        char tmp[1111] ; 
        scanf("%s", tmp) ;
        int sum = 0 ;
        int ans = 0 ;
        for(int i = 0 ; i <= sm ; i++){
            int now = tmp[i]-'0' ;
            if(i > sum){
                ans += i-sum ;
                sum = i ;
            }
            sum += now ;
        }
        printf("%d\n", ans) ;
    }
    return 0 ; 
}




