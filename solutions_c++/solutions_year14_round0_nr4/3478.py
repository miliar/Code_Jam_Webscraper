#include <iostream>
#include<stdio.h>

using namespace std;

int main(){
    FILE* fichier_in=fopen("input.txt","r");
    FILE* fichier_out=fopen("output.txt","a");
    if(fichier_in==NULL) return 0;
    int NbrCase=0;
    fscanf(fichier_in,"%d",&NbrCase);
    for(int i=0; i<NbrCase; i++){
        int NbrWood=0;
        fscanf(fichier_in,"%d",&NbrWood);
        double Naomi[NbrWood];
        for(int j=0; j<NbrWood; j++) fscanf(fichier_in,"%lf",&Naomi[j]);
        double Ken[NbrWood];
        for(int j=0; j<NbrWood; j++) fscanf(fichier_in,"%lf",&Ken[j]);

        // Sort all tables
        for(int j=0; j<NbrWood; j++){
            int MinKen=j;
            int MinNaomi=j;
            for(int k=j+1; k<NbrWood; k++){
                if(Ken[MinKen]>Ken[k]) MinKen=k;
                if(Naomi[MinNaomi]>Naomi[k]) MinNaomi=k;
            }
            double tampon=Ken[j];
            Ken[j]=Ken[MinKen];
            Ken[MinKen]=tampon;
            tampon=Naomi[j];
            Naomi[j]=Naomi[MinNaomi];
            Naomi[MinNaomi]=tampon;
        }

        // War optimally
        int position=0;
        int Win=0;
        for(int j=0; j<NbrWood; j++){
            for(int k=position; k<NbrWood; k++){
                if(Ken[position]>Naomi[j]){
                     Win++;
                     position++;
                     break;
                }
                position++;
            }
            if(position>=NbrWood) break;
        }
        int warOptimally=NbrWood-Win;

        // Deceitful War optimally
        position=0;
        Win=0;
        for(int j=0; j<=NbrWood; j++){
            for(int k=position; k<NbrWood; k++){
                if(Naomi[position]>Ken[j]){
                     Win++;
                     position++;
                     break;
                }
                position++;
            }
            if(position>=NbrWood) break;
        }
        int DecwarOptimally=Win;
        fprintf(fichier_out,"Case #%d: %d %d\n",i+1,DecwarOptimally,warOptimally);
        //printf("Case #%d: %d %d\n",i+1,DecwarOptimally,warOptimally);
    }
}
