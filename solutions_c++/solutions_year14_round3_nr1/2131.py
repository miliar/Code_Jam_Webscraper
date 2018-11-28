#include <iostream>
#include <fstream>

#include "inFileStream.hpp"

using namespace std;

#define FIN "A-small-attempt3.in"
#define FOUT "A-small-attempt3.out"

int main()
{
    inFDStream ifds(FIN);
    ifds.loadAllFile();

    ofstream myfile;
    myfile.open (FOUT);

    int T;
    ifds.getNumber(&T);

    int P;
    int Q;

    for(int t = 0; t < T; t++){
        ifds.getNumber(&P);
        ifds.getNumber(&Q);

        int i;
        bool found = false;
        for(i = 0; P != Q && !(Q % 2);){
            if(Q > P){
                Q /= 2;
                if(!found) i++;
            } else {
                found = true;
                P -= Q;
                Q /= 2;
            }
        }

        cout << i << "\n" << endl;

        myfile << "Case #" << t+1 << ": ";
        if(P != Q) myfile << "impossible" << "\n";
        else myfile << i << "\n";
    }

    myfile.close();
    return 0;
}
