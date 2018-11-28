#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
std::ifstream input("D-large.in");
std::ofstream output("output.out");
int T;
int main(){
    input>>T;
    int N;
    double *blocks1,*blocks2;
    for(int i=1;i<=T;i++){
           input>>N;
           int Ken1=0;
           int Naomi1=0;
           double *aux;
           aux=new double[1];
           blocks1=new double[N];
           blocks2=new double[N];
           for(int j=0;j<N;j++)input>>blocks1[j];
           for(int j=0;j<N;j++)input>>blocks2[j];  
           for(int j=0;j<N;j++)
                   for(int k=0;k<N;k++){
                           if(blocks1[j]>blocks1[k]){
                               *aux=blocks1[j];
                               blocks1[j]=blocks1[k];
                               blocks1[k]=*aux;
                               }
                           if(blocks2[j]>blocks2[k]){
                               *aux=blocks2[j];
                               blocks2[j]=blocks2[k];
                               blocks2[k]=*aux;
                               }
                   }
           //-------------
           double *damn;
           damn=new double[N];
           for(int j=0;j<N;j++)damn[N-1-j]=blocks1[j];
           for(int j=0;j<N;j++)blocks1[j]=damn[j];
           for(int j=0;j<N;j++)damn[N-1-j]=blocks2[j];
           for(int j=0;j<N;j++)blocks2[j]=damn[j];
           delete damn;
           //-----------
           //War
           delete aux;
           int aux1=0;
           Ken1=0;
           for(int j=0;j<N;j++)
                   for(int k=aux1;k<N;k++)
                           if(blocks1[j]<blocks2[k]){Ken1++;aux1=k+1;;break;}
           Naomi1=N-Ken1;
           //Deceithfull War
           int Naomi2=0;
           int offset=0;
           for(int j=N-1;j-offset>=0;j--){
                   if(blocks1[j]>blocks2[j-offset])Naomi2++;
                   else {offset++;j++;}
                   }
           //-----
           output<<"Case #"<<i<<": "<<Naomi2<<" "<<Naomi1<<"\n";  
    }

    return 0;
}
