#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>

using namespace std;

main(){
    ifstream in;
    ofstream out;
    in.open("input.in");
    out.open("output.out");

    int numOfCases;
    int fLine;
    int sLine;
    int times;
    int same;

    in >> numOfCases;

    int fTable[4][4];
    int sTable[4][4];

    for(int t=0; t<numOfCases; t++){
        in >> fLine;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                in >> fTable[i][j];
            }
        }
        in >> sLine;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                in >> sTable[i][j];
            }
        }

        times = 0;

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(fTable[fLine-1][i] == sTable[sLine-1][j]){
                    times++;
                    same = fTable[fLine-1][i];
                }
            }
        }

        if(times == 0){
            out << "Case #" << t+1 << ": Volunteer cheated!" << endl;
        }
        else if(times == 1){
            out << "Case #" << t+1 << ": " << same << endl;
        }
        else{
            out << "Case #" << t+1 << ": Bad magician!" << endl;
        }

    }


    system("PAUSE");
}
