
#include <cstdio>
#include <cstring>

char map[111][111] ; 
char ok[111][111] ; 
int cntR[111] ; 
int cntC[111] ; 

bool isArr(char c){
    if(c == '>' || c == '^' || c == '<' || c == 'v')
        return true ;
    return false ;
}

int main()
{
    int T ;
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ; 
        int R, C ;
        scanf("%d%d", &R, &C) ; 
        for(int i = 0 ; i != R ; i++){
            scanf("%s", map[i]) ; 
        }
        memset(ok, false, sizeof(ok)) ; 
        for(int i = 0 ; i != R ; i++){
            bool lf = false ; 
            for(int j = 0 ; j != C ; j++){
                if(lf && map[i][j] == '<')
                    ok[i][j] = true ;
                if(isArr(map[i][j]))
                    lf = true ;
            }
            bool rt = false ;
            for(int j = C-1 ; j >= 0 ; j--){
                if(rt && map[i][j] == '>')
                    ok[i][j] = true ;
                if(isArr(map[i][j]))
                    rt = true ;
            }
        }
        for(int j = 0 ; j != C ; j++){
            bool tp = false ;
            for(int i = 0 ; i != R ; i++){
                if(tp && map[i][j] == '^')
                    ok[i][j] = true ;
                if(isArr(map[i][j]))
                    tp = true ;
            }
            bool dn = false ;
            for(int i = R-1 ; i >= 0 ; i--){
                if(dn && map[i][j] == 'v')
                    ok[i][j] = true ;
                if(isArr(map[i][j]))
                    dn = true ;
            }
        }
        memset(cntR, 0, sizeof(cntR)) ; 
        memset(cntC, 0, sizeof(cntC)) ; 
        for(int i = 0 ; i != R ; i++){
            for(int j = 0 ; j != C ; j++)
                if(isArr(map[i][j]))
                    cntR[i]++ ;
        }
        for(int j = 0 ; j != C ; j++){
            for(int i = 0 ; i != R ; i++)
                if(isArr(map[i][j]))
                    cntC[j]++ ;
        }
        int ans = 0 ; 
        bool ex = true ;
        for(int i = 0 ; i != R ; i++){
            for(int j = 0 ; j != C ; j++){
                if(ok[i][j])
                    continue ; 
                if(isArr(map[i][j])){
                    if(cntR[i] == 1 && cntC[j] == 1){
                        ex = false ;
                    }
                    ans++ ;
                }
            }
        }
        if(ex)
            printf("%d\n", ans) ;
        else
            puts("IMPOSSIBLE") ; 
    }
    return 0 ; 
}
