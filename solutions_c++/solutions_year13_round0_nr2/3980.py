#include <stdio.h>

int lawn[102][102];

bool revisa(int fila, int col, int a, int b){
    int num = lawn[fila][col];
    bool fil = true, columna = true;
    
    for(int j = 0; j < a; j++){
        if(lawn[j][col] > num){
            columna = false;
        }
    }
    
    for(int j = 0; j < b; j++){
        if(lawn[fila][j] > num)
            fil = false;
    }
    
    if(!columna && !fil){
        //printf("Fila %d, Columa %d\n", fila, col);
        return false;
    }
    return true;
}

void imprime(int a, int b){
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++)
            printf("%d ", lawn[i][j]);
        printf("\n");
        }
}

int main(){
    int T;
    int a, b;
    bool sePuede;
    
    scanf("%d", &T);
    
    for(int i = 1; i <= T; i++){
        sePuede = true;
        scanf("%d%d", &a, &b);
        
        for(int j = 0; j < a; j++){
            for(int k = 0; k < b; k++){
                scanf("%d", &lawn[j][k]);
            }
        }
        
        //imprime(a, b);
        
        for(int j = 0; j < a; j++){
            for(int k = 0; k < b; k++){
                if(!revisa(j, k, a, b)){
                    sePuede = false;
                }
            }
        }
        
        printf("Case #%d: ", i);
        if(sePuede)
            puts("YES");
        else
            puts("NO");
    }
    
    
    return 0;
}
