#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{

    FILE* fichier_in=fopen("input.txt","r");
    FILE* fichier_out=fopen("output.txt","a");
    if(fichier_in==NULL) return 0;
    int NbrCase=0;
    fscanf(fichier_in,"%d",&NbrCase);
    int Possibilite[4][2];
    int choix=0;
    int tampon=0;
    for(int i=0; i<NbrCase; i++){
        for(int l=0; l<2; l++){
            fscanf(fichier_in,"%d",&choix);
            int p=0;
            for(int j=1; j<=4; j++)for(int k=0; k<4; k++){
                if(j==choix)fscanf(fichier_in,"%d",&Possibilite[k][l]);
                else fscanf(fichier_in,"%d",&tampon);
            }
        }
        int result=0, nbrMatch=0;
        for(int j=0; j<4; j++) for(int k=0; k<4; k++)if(Possibilite[j][0]==Possibilite[k][1]){
            result=Possibilite[j][0];
            nbrMatch++;
        }

        if(nbrMatch!=1) fprintf(fichier_out,"Case #%d: %s\n",i+1,nbrMatch==0?"Volunteer cheated!":"Bad magician!");
        else fprintf(fichier_out,"Case #%d: %d\n",i+1,result);
    }
    return 0;
}
