#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

// bool myfunction (int i,int j) { return (i<j); }

bool isContained(float num, vector<float> kenVec){
    //cout << kenVec.size() << endl;
    for (int i = 0; i < kenVec.size(); i++){
        //cout << "in the condition" << endl;
        if (num == kenVec[i]) return true;
        //cout << "after the condition" << endl;
    }
    return false;
}

int main(){
    int numCases;

    FILE* fin = fopen("D-large.in", "r");
    fscanf(fin, "%d\n", &numCases);
    ofstream fout;
    fout.open("outnew.out");

    for (int i = 0; i < numCases; i++){
        int normResult = 0;
        int chResult = 0;

        int numWeights;
        fscanf(fin, "%d", &numWeights);

        vector<float> namVec(numWeights), workNam(numWeights);
        vector<float> kenVec(numWeights), workKen(numWeights);

        for (int j = 0; j < numWeights; j++){
            fscanf(fin, "%f", &namVec[j]);
        }

        for (int j = 0; j < numWeights; j++){
            fscanf(fin, "%f", &kenVec[j]);
        }

        sort(namVec.begin(), namVec.end());

        sort(kenVec.begin(), kenVec.end());

        vector<float> nam2 = namVec;
        workNam = nam2;
        vector<float> ken2 = kenVec;
        workKen = ken2;

        vector<bool> truthVector(numWeights);

        for (int boolit = 0; boolit < numWeights; boolit++){
            truthVector[boolit] = true;
        }

        // block for computing normResult
        normResult = numWeights;

        for (int index = 0; index < numWeights; index++){
            for (int index2 = 0; index2 < numWeights; index2++){

                if (workKen[index2] > workNam[index] && truthVector[index2]){
                    normResult--;
                    truthVector[index2] = false;
                    index2 = 0;
                    break;
                }
            }

        }

        // block for computing chResult

        for (int comp4 = 0; comp4 < numWeights; comp4++){
            if (nam2[0] > ken2[0]) {
                nam2.erase(nam2.begin());
                chResult++;
                ken2.erase(ken2.begin());
            }
            else {
                nam2.erase(nam2.begin());
                ken2.erase(ken2.begin() + (ken2.size()-1));
            }
        }

        fout << "Case #" << i+1 << ": " <<chResult << " " << normResult << endl;
    }

    return 0;
}
