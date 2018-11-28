#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>

typedef long long t;

using namespace std;


void process(int C){
    int A,i,j,Sena[27] = {},Sum = 0;
    int Q[3], start =0;
    scanf("%d",&A);
    for(i=0;i<A;i++){
        scanf("%d",&Sena[i]);
        Sum += Sena[i];
    }
    printf("Case #%d:", C);
    while(Sum > 0){
        int M = 0, D1 =-1,D2=-1;
        for(i=0;i<A;i++){
            if(Sena[i] > M || i==0){
                D1 = i;
                M = Sena[i];
            }
            else if(Sena[i] == M){
                D2 = i;
            }
        }
        printf(" ");
        Sena[D1]--;
        Sum--;
        printf("%c",D1+'A');
        if(D2 > -1 && Sum != 2){
            Sum--;
            Sena[D2]--;
            printf("%c",D2+'A');
        }

    }
    printf("\n");
}

int main(){
    //read
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        //output
        process(i);
    }
}
