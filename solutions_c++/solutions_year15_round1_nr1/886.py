#include<stdio.h>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
vector<int> Pole;
int main(void){
    FILE *fin=fopen("A-large.in", "r");
    FILE *fout=fopen("A-large.out", "w");
    int T;
    int i;
    fscanf(fin,"%i", &T);
    int N;
    int j;
    int c;
    int prvni;
    int druhy;
    int maxi;
    for(i=0;i<T;i++){
        prvni=0;
        druhy=0;
        maxi=0;
        Pole.clear();
        fscanf(fin, "%i", &N);
        for(j=0;j<N;j++){
            fscanf(fin, "%i", &c);
            Pole.push_back(c);
        }
        for(j=0;j<N-1;j++){
            if(Pole[j+1]<Pole[j]) {prvni+=Pole[j]-Pole[j+1];
                if(Pole[j]-Pole[j+1]>maxi) maxi=Pole[j]-Pole[j+1];}
        }
        for(j=0;j<N-1;j++){
            if(Pole[j]<maxi) druhy+=Pole[j];
            else druhy+=maxi;
        }
        fprintf(fout, "Case #%i: %i %i\n", i+1, prvni, druhy);
    }
    return 0;
}
