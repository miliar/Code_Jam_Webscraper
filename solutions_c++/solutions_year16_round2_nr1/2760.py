#include <cstdio>
#include <cstring>

using namespace std;

char algarisms[][10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

char S[2020];
int numbs[10];

void parse(int alg, char x){
    int i, j, tamsrc, tamtarget = strlen(algarisms[alg]);
    int tam = strlen(S);
    for(i=0; i<tam; i++){
        if(S[i] == '*') continue;
        if(S[i] == x){
            j = -1;
            tamsrc = 0;
            while(tamsrc<tamtarget){
                j++;
                if(j>tam)
                    j=0;
                if(S[j] == algarisms[alg][tamsrc]){
                    S[j] = '*';
                    tamsrc++;
                    j = -1;
                }
            }
            numbs[alg]++;
        }
    }
    return;
}


int main() {
    int T, at=0;
    scanf("%d\n", &T);
    while(at<T){
        memset(numbs, 0, sizeof(numbs));    
        fgets(S, 2010, stdin);
        parse(0, 'Z');
        //printf("procurando 0");
        parse(2, 'W');
        //printf("procurando 2");
        parse(4, 'U');
        //printf("procurando 4");
        parse(6, 'X');
        //printf("procurando 3");
        parse(8, 'G');
        //printf("procurando 8");
        parse(3, 'H');
        //printf("procurando 6");
        parse(5, 'F');
        //printf("procurando 5");
        parse(7, 'V');
        //printf("procurando 7");
        parse(9, 'I');
        //printf("procurando 9");
        parse(1, 'O');
        at++;
        printf("Case #%d: ", at);
        for(int i=0; i<10; i++)
            for(int j=0; j<numbs[i]; j++)
                printf("%d", i);
        printf("\n");
        //print resposta \n
    }
    return 0;
}
