#include <iostream>
#include <fstream>

using namespace std;

int main(void){

ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");

int T;
fin >> T;

for(int i=0; i<T; i++){

    int answer_a, answer_b;

    fin >> answer_a;
    answer_a -= 1; //our row starts at 0
    int arrangement_a[4][4];
    int arrangement_b[4][4];
    //Grab first arrangement
    for(int j=0; j<4; j++){
        for(int k=0; k<4; k++){
            fin >> arrangement_a[j][k];
        }
    }
     //Grab second arrangement
    fin >> answer_b;
    answer_b -= 1;
    for(int j=0; j<4; j++){
        for(int k=0; k<4; k++){
            fin >> arrangement_b[j][k];
        }
    }

    int cards_possible = 0, cardfound =0;

    for(int j=0; j<4; j++){
        for(int k=0; k<4; k++){
            if(arrangement_a[answer_a][j] == arrangement_b[answer_b][k]){
                cardfound = arrangement_a[answer_a][j];
                cards_possible++;
            }
        }
    }
    if(cards_possible == 1){
        fout << "Case #" << (i+1) << ": " << cardfound;
    }
    else if(cards_possible > 1){
        fout << "Case #" << (i+1) << ": Bad magician!";
    }
    else{
        fout << "Case #" << (i+1) << ": Volunteer cheated!";
    }

    if(i!=(T-1)){
        fout << endl;
    }
}



return 0;
}
