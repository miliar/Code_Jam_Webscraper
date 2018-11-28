#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ofstream fout("A-small-attempt0.out");
    ifstream fin("A-small-attempt0.in");
    int T;
    fin>>T;
    for(int i=1; i<=T; i++){
        int answer1, answer2, data[4], count=0, number, answerNum=0, answer=0;
        fin>>answer1;
        while(count < 16){
            fin>>number;
            if((count/4+1) == answer1){
                data[count%4] = number;
            }
            count++;
        }

        fin>>answer2;
        count = 0;
        while(count < 16){
            fin>>number;
            if((count/4+1) == answer2){
                for(int j=0; j<4; j++){
                    if(data[j] == number){
                        answerNum++;
                        answer = number;
                        break;
                    }
                }
            }
            count++;
        }

        if(answerNum == 1){
            fout<<"Case #"<<i<<": "<<answer<<endl;
        }
        else if(answerNum > 1){
            fout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        }
        else if(answerNum == 0){
            fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }
    }
    fin.close();
    fout.close();

    return 0;
}
