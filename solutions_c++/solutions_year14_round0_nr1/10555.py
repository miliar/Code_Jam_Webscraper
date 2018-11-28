#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]){
    ifstream fcin(argv[1]);
    int cases;
    fcin >> cases;
    int i = 0;

    while (i < cases){
        int row1;
        fcin >> row1;
        row1--;
        vector< vector <int> > cards1(4);

        for ( int j = 0 ; j < 4 ; j++ )
            cards1[j].resize(4);

        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                fcin >> cards1[j][k];
            }
        }

        int row2;
        fcin >> row2;
        row2--;
        vector< vector <int> > cards2(4);

        for ( int j = 0 ; j < 4 ; j++ )
            cards2[j].resize(4);

        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                fcin >> cards2[j][k];
            }
        }
        int iguais = 0;
        int card = 0;
        for(int j = 0; j < 4; j++){
          for(int k = 0; k < 4; k++){
              if(cards1[row1][j] == cards2[row2][k]){
                  iguais++;
                  card = cards1[row1][j];
              }
          }
        }

        if(iguais == 0) cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        if(iguais == 1) cout << "Case #" << i+1 << ": " << card << endl;
        if(iguais >= 2) cout << "Case #" << i+1 << ": Bad magician!" << endl;

        i++;
    }

return 0;
}




