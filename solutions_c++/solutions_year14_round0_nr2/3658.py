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
        double C,F,X;
        double result=0;
        fscanf(fichier_in,"%lf %lf %lf",&C,&F,&X);
        double product=2;
        int nbrFarm=0;
        while (true){
            double theTime=((C-X)/product)+(X/(product+F));
            if(theTime>=0){
                result+=(X/product);
                break;
            } else result+=(C/product);
            nbrFarm++;
            product+=F;
        }
        fprintf(fichier_out,"Case #%d: %.7lf\n",i+1,result);
        //printf("Case #%d: %.7lf\n",i+1,result);
    }
}
