#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include <fstream>
using namespace std;
int main(){
    ifstream read;
    read.open("B-large.in");
    ofstream write;
    write.open("answer.txt");
    int caseNo;
    read >> caseNo;
    for(int i = 1; i <= caseNo; i++){

        int height, width;
        read >> height >> width;
        int matrix[height][width];
        for(int j = 0; j < height; j++){
            for(int k = 0; k < width; k++){
                read >> matrix[j][k];
            }
        }
        bool possible = true;
        for(int j = 0; j < height; j++){
            for(int k = 0; k < width; k++){
                //cout << j << " " << k << endl;
                int choosen = matrix[j][k];
                bool pass = true;
                //horizon
                for(int l = 0; l < width; l++){
                    if(matrix[j][l] > choosen){
                        //if(i == 6)cout << j << " " << k << endl;
                        pass = false;//cout << "!";
                        break;
                    }
                }
                if(pass)continue;
                pass = true;
                //vertical
                for(int l = 0; l < height; l++){
                    if(matrix[l][k] > choosen){
                        if(i == 6)cout << j << " " << k << endl;
                        pass = false;
                        break;
                    }
                }
                if(pass)continue;
                else{
                    possible = false;
                    break;
                }
            }
            if(!possible)break;
        }
        write << "Case #" << i << ": ";
        if(possible)write << "YES";
        else write << "NO";
        write << endl;
    }
    return 0;
}
