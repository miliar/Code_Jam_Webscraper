#include<iostream>
#include<fstream>
#include<iomanip>
#include <stdio.h>
#include<stdlib.h>
using namespace std;


ifstream fin("B-large.in");




int main(){
    FILE *fout;
    fout = fopen("B-large.out","w");
    int numcase;
    fin>>numcase;
    int countcase = 1;
    double C,F,X;
    double prevmin;
    double curmin ;
    double ability;
    double buyfarm;

    while(countcase<=numcase){
        fin>>C>>F>>X;
        prevmin = 0;
        curmin = 0;
        ability = 2;
        buyfarm = 0;

        while(curmin<=prevmin){
             if(curmin == 0)
                prevmin += 1.000000*X/ability;
             else
                prevmin = 1.000000*buyfarm+ 1.000000*X/(ability);
             if(C>X)break;

             curmin = 1.000000*buyfarm+1.000000*C/ability+1.000000*X/(ability+F);
             buyfarm += 1.000000*C/ability;

             ability += F;

        }
        fprintf(fout,"Case #%d: %f8\n",countcase,prevmin);
        //fout<<"Case #"<<countcase<<": "<<inputup<<"."<<inputdown<<endl;
        countcase++;

    }
}
