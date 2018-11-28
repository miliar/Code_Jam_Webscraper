#include <iostream>
#include <string>
using namespace std;

int FindMoves (string input){
    bool Plus = false;
    bool checkNeg = false;
    int sum_move = 0;
    //char myArray[input.size()+1];
    //strcpy(myArray,input.c_str());

    for(int i =0;i<input.length();i++){
        if(input[i] == '+'){
            Plus = true;
            if(checkNeg){
                sum_move++;
                checkNeg = false;
            }
        }else{
            if(Plus){
                sum_move++;
                checkNeg = true;
                Plus = false;
            }
            checkNeg = true;
        }
    }

    if(checkNeg){
        sum_move++;
    }
    return sum_move;

}

int main(){
    string input;
    int T = 0;
    int moves = 0;
    int testC = 0;

    cin >> T;
    for(int i =0;i<T;i++){
        cin>>input;
        moves = FindMoves(input);
        testC = i+1;
        cout<<"Case #"<<testC<<": "<<moves<<endl;
    }
    return 0;
}


