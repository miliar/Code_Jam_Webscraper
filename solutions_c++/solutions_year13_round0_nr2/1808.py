#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;

const string YES = "YES";
const string NO = "NO";

int desiredLawn[109][109];

bool check(int value, int i, int j, int N, int M){
    bool canCutRow = true;

    for (int k = 0; k < M; k++){
        if (desiredLawn[i][k] > value){
            canCutRow = false;
        }
    }

    bool canCutColumn = true;

    for (int k = 0; k < N; k++){
        if (desiredLawn[k][j] > value){
            canCutColumn = false;
        }
    }

    return canCutRow || canCutColumn;
}

bool solve(int N, int M){

    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            if (!check(desiredLawn[i][j], i, j, N, M)){
                return false;
            }
        }
    }

    return true;

}

int main(){

    ifstream in("B-large.in");
    ofstream out("B-large.out");

    int T;
    in >> T;

    int caseNumber;

    for (caseNumber = 1; caseNumber <= T; caseNumber++){
        int N, M;

        //input
        in >> N >> M;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                in >> desiredLawn[i][j];
            }
        }

        //output
        out << "Case #" << caseNumber << ": ";
        if (solve(N, M)){
            out << YES;
        }
        else{
            out << NO;
        }

        out << endl;
    }


    in.close();
    out.close();
    return 0;
}
