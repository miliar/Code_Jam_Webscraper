#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main()
{
    int i=0;
    int j=0;
    int k=0;
    int loop=0;
    int linhaA=0;
    int linhaB=0;
    int vA[4] = {0,0,0,0};
    int vB[4] = {0,0,0,0};
    int temp1=0;
    int temp2=0;
    int temp3=0;
    int temp4=0;
    int cont=0;
    int carta=0;

    cin >> loop;

    for(i=0;i<loop;i++){

        cin >> linhaA;

        for(j=1;j<=4;j++){
            scanf("%d %d %d %d", &temp1, &temp2, &temp3, &temp4);
            if(j==linhaA){
                vA[0]=temp1;
                vA[1]=temp2;
                vA[2]=temp3;
                vA[3]=temp4;
            }
        }

        cin >> linhaB;

        for(j=1;j<=4;j++){
            scanf("%d %d %d %d", &temp1, &temp2, &temp3, &temp4);
            if(j==linhaB){
                vB[0]=temp1;
                vB[1]=temp2;
                vB[2]=temp3;
                vB[3]=temp4;
            }
        }
        cont=0;
        for(k=0;k<4;k++){
            for(j=0;j<4;j++){
                if(vA[k]==vB[j]){
                    cont=cont+1;
                    carta=vA[k];
                }
            }
        }

        if(cont==0) printf("Case #%d: Volunteer cheated!\n", i+1);
        if(cont==1) printf("Case #%d: %d\n", i+1, carta);
        if(cont>1) printf("Case #%d: Bad magician!\n", i+1);

    }



}
