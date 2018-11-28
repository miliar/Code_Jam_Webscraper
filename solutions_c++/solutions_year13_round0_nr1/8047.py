#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int notComplete(char table[4][4]);
bool winner(char table[4][4],char c);
int main (int argc,char *argv[]){

    int T;
    char table[4][4];
    ifstream file("A-small-attempt.in");
    ofstream file2("output.in");
    file >> T;
    if(file){
        for(int j=1;j<=T;j++){
            for(int i=0;i<4;i++){

                    file >> table[i][0];
                    file >> table[i][1];
                    file >> table[i][2];
                    file >> table[i][3];

            }
            string cas;
            if(file2){
                cas = "Case #";


                    if(winner(table,'X'))
                        file2 << cas << j << ": " << "X won" <<endl;
                    else
                        if(winner(table,'O'))
                         file2 << cas << j << ": " << "O won" <<endl;
                        else
                            if(notComplete(table)>0)
                                file2 << cas << j << ": " << "Game has not completed" <<endl;
                            else
                                file2 << cas << j << ": " << "Draw" <<endl;

            }
            else
            {
                cout << "ERROR : ouverture impossible 2";
                return 0;
            }

        }
    }
    else
    {
        cout << "ERROR : ouverture impossible 1";
        return 0;
    }




}

bool winner(char table[4][4],char c) {
    bool w = false;
    int j=0;
    int comptCol;
    int comptLig;
    int comptDiag1=0;
    int comptDiag2=0;


    while(j<4 && w == false){
        comptCol=0;
        comptLig=0;
        for(int i=0;i<4;i++){
            //calcul diagonale principale
            if(j == 0){
                if(table[i][i] == c){
                        comptDiag1++;
                    }else if(table[i][i] == 'T'){
                        comptDiag1--;
                    }else comptDiag1 = comptDiag1 -6;
                    if(table[i][3-i] == c){
                            comptDiag2++;
                        }else if(table[i][3-i] == 'T'){
                            comptDiag2--;
                        }else
                            comptDiag2 = comptDiag2-6;

            }
            //calcul collone
            if(table[i][j]==c)
                comptCol++;
            else if(table[i][j]== 'T'){
                comptCol--;
            }else comptCol =comptCol-6;
            //calcul ligne
            if(table[j][i]==c)
                comptLig++;
            else if(table[j][i]== 'T'){
                comptLig--;
            }else comptLig= comptLig - 6;

        }
         if((comptCol==2||comptDiag1==2||comptDiag2==2||comptLig==2)||(comptCol==4||comptDiag1==4||comptDiag2==4||comptLig==4)){
               w = true;
         }
         j++;
    }
    return w;
}

int notComplete(char table[4][4]){
    int comptPoint=0;
    for(int i=0;i<4;i++){
        comptPoint=0;
        for(int j=0;j<4;j++){
            if(table[i][j]=='.')
                comptPoint++;

        }
    }

        return comptPoint;

}

