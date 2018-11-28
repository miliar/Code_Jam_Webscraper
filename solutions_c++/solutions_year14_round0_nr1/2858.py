#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int card[4][4], p[17];

int main(){
    ios::sync_with_stdio(false);
    int t, chooseNumber1, chooseNumber2, countP, answer;
    fstream file, file2;
    file2.open("A-small-attempt2.in");
    file.open("output.txt", ios::out);
    if(file2.is_open()){
        file2 >> t;
        for(int c=1 ; c<=t ; c++){
            file2 >> chooseNumber1;
            for(int i=0 ; i<4 ; i++){
                for(int j=0 ; j<4 ; j++){
                    file2 >> card[i][j];
                    p[card[i][j]]=i+1;
                }
            }

            file2 >> chooseNumber2;
            for(int i=0 ; i<4 ; i++){
                for(int j=0 ; j<4 ; j++){
                    file2 >> card[i][j];
                }
            }

            countP=0;
            for(int i=0 ; i<4 ; i++){
                if(p[card[chooseNumber2-1][i]]==chooseNumber1){
                    countP++;
                    answer=card[chooseNumber2-1][i];
                }
                if(countP>1)
                    break;
            }

            file << "Case #" << c << ": ";
            if(countP==0)
                file << "Volunteer cheated!" << endl;
            else if(countP>1)
                file << "Bad magician!" << endl;
            else
                file << answer << endl;
        }
    }
    file.close();
    file2.close();
}
