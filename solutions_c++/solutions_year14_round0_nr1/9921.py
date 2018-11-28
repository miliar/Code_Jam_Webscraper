#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

int main () {
    
    
    string line;
    ifstream myfileIn ("hello.txt");
    
    int num, cases, auxArray,aux2Array, rows, cols, ans1, ans2, finded, auxFind;
    int matrixOrigen[4];
    int matrixDest[4];
    char outline[50];
    int numCases = 0;
    ofstream myfileOut;
    myfileOut.open ("outline.out");

    if (myfileIn.is_open()) {
        num = 1, auxArray = 0, aux2Array = 0;
        
        while ( getline (myfileIn,line) ) {
            
            if (num == 1) {
                
                cases = atoi(line.c_str());
            } else {
                
                if (auxArray == 0) {
                    ans1 = atoi(line.c_str());
                } else {
                    if (auxArray == ans1) {
                        string arr[4];
                        int i = 0;
                        stringstream ssin(line);
                        while (ssin.good() && i < 4){
                            ssin >> arr[i];
                            ++i;
                        }
                        for(i = 0; i < 4; i++){
                            
                            matrixOrigen[i] = atoi(arr[i].c_str());
                            
                        }
                    }
                }
                auxArray++;

                if (auxArray > 5) {
                    if (aux2Array == 0) {
                        ans2 = atoi(line.c_str());
                    }else{
                        if (aux2Array == ans2) {
                            string arr[4];
                            int i = 0;
                            stringstream ssin(line);
                            while (ssin.good() && i < 4){
                                ssin >> arr[i];
                                ++i;
                            }
                            for(i = 0; i < 4; i++){
                                
                                
                                matrixDest[i] = atoi(arr[i].c_str());
        
                            }
                            
                        }
                    }
                    aux2Array++;
                }
                if (aux2Array > 4) {
                    aux2Array = 0;
                }
                
                auxFind = 0;
                int i = 0;
                int j = 0;
                if (auxArray >= 10) {
                    numCases ++;

                    for (i = 0; i < 4; ++i) {
                        for (j = 0; j < 4; ++j) {
                            if(matrixOrigen[i] == matrixDest[j]) {
                                auxFind++;
                                finded = matrixOrigen[i];
                            }
                        }
                    }
                    
                    switch (auxFind){
                        case 0:
                            myfileOut << "Case #" << numCases << ":" <<" Volunteer cheated!"<<endl; 
                        break;
                        case 1:
                            myfileOut << "Case #" << numCases << ": " << finded <<endl; 
                            
                        break;
                        default:
                            myfileOut << "Case #" << numCases << ":" <<" Bad magician!"<<endl; 
                    }
                    auxArray = 0;
                }
            }
            num++;
        }
    } else {
        cout << "Unable to open file";
    }

    myfileOut.close();

    return 0;

}