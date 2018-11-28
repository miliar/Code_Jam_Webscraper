#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>

using namespace std;

int main(){
ifstream input("B-large.in") ;
ofstream output("B-large.out") ;

int nbrCas;
input>>nbrCas;

for(int k(0); k<nbrCas; k++){
    double C,F,X;
    double gainS=2,time=0;
    input>>C>>F>>X;


        while(1){
            double temp;temp= (double) X/gainS;
            double temp2;temp2= (((double) C/gainS) + ((double) X/(gainS+F)));
            if(temp<temp2){
                time+=temp;
                output<<"Case #"<<k+1<<": "<<fixed<<time;
                break;
            }
            else{
                time+= (float) C/gainS;
                gainS+=F;
            }

        }
        if(k != nbrCas-1)
            output<<endl;
}

}


