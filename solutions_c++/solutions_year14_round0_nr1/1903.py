#include<iostream>
using namespace std;

int main(){
    int input1[16], input2[16], guess1[4], guess2[4];
    int count, answer1, answer2, i, j, k, possible, track;
    
    cin >> count;
    for(i = 1; i <= count; i++){
        possible = 0;
        cin >> answer1;
        for(j = 0; j < 16; j++){
            cin >> input1[j];
        }
        cin >> answer2;
        for(j = 0; j < 16; j++){
            cin >> input2[j];
        }
        for(j = 4 * (answer1 - 1); j <= 4 * answer1 - 1; j++){
            guess1[j % 4] = input1[j];
        }
        for(j = 4 * (answer2 - 1); j <= 4 * answer2 - 1; j++){
            guess2[j % 4] = input2[j];
        }
        for(j = 0; j < 4; j++){
            for(k = 0; k < 4; k++){
                if(guess1[j] == guess2[k]){
                    possible++;
                    track = guess1[j];
                }
            }
        }
        if(possible == 1){
            cout << "Case #" << i << ": " << track << endl;
        }
        else if(possible < 1){
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
        }
        else{
            cout << "Case #" << i << ": Bad magician!" << endl;
        }
    }
    return 0;
}
