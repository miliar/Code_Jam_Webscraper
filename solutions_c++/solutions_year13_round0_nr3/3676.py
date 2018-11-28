#include <stdio.h>
#include <cmath>
#include <cstring>

using namespace std;

bool palindromo(char cadena[]){
    int longi = strlen(cadena);
    for(int i = 0, j = longi - 1; i < j; i++, j--)
        if(cadena[i] != cadena[j])
            return false;
    return true;
}

int main(){
    int T;
    long long int a, b, acum, root;
    char numero[15];
    char raiz[15];
    
    scanf("%d", &T);
    
    for(int i = 1; i <= T; i++){
        acum = 0;
        scanf("%lld%lld", &a, &b);
        
        for(long long int j = a; j <= b; j++){
            sprintf(numero, "%lld", j);
            
            root = (long long int)sqrt(j);
            if(root * root != j)
                root = 12;
            
            
            sprintf(raiz, "%lld", root);
        
            if(palindromo(numero) && palindromo(raiz))
                acum++;
        }
        
        printf("Case #%d: %lld\n", i, acum);
        
    }
    
    
    return 0;
}
