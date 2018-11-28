#include <cstdio>
#include <cstring>

int qd(int n, int p){
    return p == 0 ? n%10 : qd(n/10, p-1);
}

int nd(int n){
    return n < 10 ? 1 : nd(n/10)+1;
}

int main(){
    int t, nd_n, j = 1, casos = 1;
    long long n = 0, atual;
    int marcados[11] = {0};
    bool todos_visitados;

    scanf("%d", &t);

    while(t--){
        scanf("%lld", &n);
        if(n == 0){
            printf("Case #%d: INSOMNIA\n", casos++);
        }
        else{
            todos_visitados = false;
            memset(marcados, 0, sizeof marcados);
            j = 1;
            while(!todos_visitados){
                atual = j*n; j++;
                nd_n = nd(atual);
                for(int i = 0 ; i < nd_n ; i++){
                    marcados[qd(atual, i)] = 1;
                    //printf("marcou: %d\n", qd(atual, i));
                }
                //printf("\n");
                todos_visitados = true;
                for(int i = 0 ; i < 10 && todos_visitados ; i++){
                    if(!marcados[i]){
                        todos_visitados = false;
                    }
                }
            }
            printf("Case #%d: %lld\n", casos++, atual);
        }
    }

    return 0;
}
