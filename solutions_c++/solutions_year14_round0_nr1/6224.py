#include <iostream>

using namespace std;

int main(){
    int numCase;
    cin >> numCase;
    for (int i=1; i<=numCase; i++){
        int temp, choice, answer;
        int numAnswer=0;
        int first[4];
        int second[4];
        //for each case
        //first answer
        cin >> choice;
        for (int row=0; row<4; row++){
            for (int col=0; col<4; col++){
                if (row==(choice-1)){
                    cin >> first[col];
                    //cout << first[col];
                }else
                    cin >> temp;
            }
        }
        //second answer
        cin >> choice;
        for (int row=0; row<4; row++){
            for (int col=0; col<4; col++){
                if (row==(choice-1)){
                    cin >> second[col];
                    //cout << second[col];
                }else
                    cin >> temp;
            }
        }
        //compare
        for (int a=0; a<4; a++){
            for (int b=0; b<4; b++){
                if(first[a]==second[b]){
                    answer = first[a];
                    numAnswer++;
                }
            }
        }
        if (numAnswer==0)
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
        if (numAnswer==1)
            cout << "Case #" << i << ": " << answer << endl;
        if (numAnswer>1)
            cout << "Case #" << i << ": Bad magician!" << endl;
        
    }
    return 0;
}
