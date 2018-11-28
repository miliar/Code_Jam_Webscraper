#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream read;
    ofstream write;

    read.open("A-small-attempt0.txt");
    write.open("output.txt");

    int test;
    read >> test;


    for(int testing=0; testing <test; testing++){

    int array1[4][4], array2[4][4], narr1[4], narr2[4];
    int ans1, ans2, match=0, answer;

    read >> ans1;
    for(int i=0; i<4;i++){
        for(int j=0; j<4; j++){
            read >> array1[i][j];
        }
    }

    read >> ans2;
    for(int i=0; i<4;i++){
        for(int j=0; j<4; j++){
            read >> array2[i][j];
        }
    }

    for(int i=ans1-1; i<ans1; i++){
        for(int j=0; j<4; j++){
            narr1[j] = array1[i][j];
        }
    }

    for(int i=ans2-1; i<ans2; i++){
        for(int j=0; j<4; j++){
            narr2[j] = array2[i][j];
        }
    }

    for (int i=0;i<4;++i){
        for (int j=0;j<4;++j){
            if (narr1[i] == narr2[j]){
                match ++;
                answer = narr1[i];
              }
            }
        }

    write << "Case #" << testing+1 << ": ";
    if(match > 1) write << "Bad magician!";
    if(match < 1) write << "Volunteer cheated!";
    if(match == 1) write << answer;
    write << endl;

    }

 system("pause");
 return 0;
 }
