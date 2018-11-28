
#include <cstdio>
#include <cstring>

int app[22] ;

int main()
{
    int T ;
    scanf("%d", &T) ;
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ;
        int fa ;
        scanf("%d", &fa) ;
        memset(app, 0, sizeof(app)) ;
        for(int i = 1 ; i <= 4 ; i++){
            if(i == fa){
                for(int j = 0 ; j != 4 ; j++){
                    int now ;
                    scanf("%d", &now) ;
                    app[now] = true ;
                }
            }
            else{
                scanf("%*d%*d%*d%*d") ;
            }
        }
        int sa ;
        scanf("%d", &sa) ;
        int ans, cnt = 0 ;
        for(int i = 1 ; i <= 4 ; i++){
            if(i == sa){
                for(int j = 0 ; j != 4 ; j++){
                    int now ;
                    scanf("%d", &now) ;
                    if(app[now]){
                        ans = now ;
                        cnt++ ;
                    }
                }
            }
            else{
                scanf("%*d%*d%*d%*d") ;
            }
        }
        if(cnt == 1)
            printf("%d\n", ans) ;
        else if(cnt)
            puts("Bad magician!") ;
        else
            puts("Volunteer cheated!") ;
    }
    return 0 ;
}
