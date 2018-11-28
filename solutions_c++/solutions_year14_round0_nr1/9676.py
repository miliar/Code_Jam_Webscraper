#include <cstdio>

using namespace std;

int nums[16];
int cartas[4][4];

void limpia(){
    for(int i = 0; i < 16; i++)
        nums[i] = 0;
}

int numDos(){
    int a = 0;
    for(int i = 0; i < 16; i++)
        if(nums[i] >= 2)
            a++;
    //printf("Repeticiones %d\n", a);
    return a;
}

int num(){
    for(int i = 0; i < 16; i++)
        if(nums[i] >= 2)
            return (i + 1);
}

void imprimeRespuesta(int rep, int nume, int i){
    if(rep == 1) 
        printf("Case #%d: %d\n", i, nume);
    if(rep == 0)
        printf("Case #%d: Volunteer cheated!\n", i);
    if(rep >= 2)
        printf("Case #%d: Bad magician!\n", i);
}

void debug(){
    for(int i = 0; i < 16; i++)
        printf("%d: %d\n", i + 1, nums[i]);
}

void lee(){
    int N;
    scanf("%d", &N);
    for(int j = 0; j < 4; j++)
        for(int k = 0; k < 4; k++)
            scanf("%d", &cartas[j][k]);
    for(int i = 0; i < 4; i++)
        nums[ cartas[N - 1][i] - 1]++;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        limpia();
        lee();
        lee();
        //debug();
        imprimeRespuesta(numDos(), num()  ,i+1);
    }
    
    
    return 0;
}
