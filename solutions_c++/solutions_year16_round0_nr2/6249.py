#include <iostream>
#include <sstream>
#include <string>

int currentPoint;
long int totalFlips = 0;
using namespace std;

bool checkBegin(string s);
string getWhatMatters(string input);
string doMovement(string pancakeStack);
bool checkHappiness(string pancakeStack);
int workfor2(string s);
bool checkPlus(string s);


int main(){
    int t;
    cin >> t;
    for(long long int i = 0;i< t; i++){
        string s;
        cin >> s;
        if(checkPlus(s)){
            cout << "Case #" << i+1 << ": 0" << endl;
        }
        else if(s.length() == 2){
            int result = workfor2(s);
            cout << "Case #" << i+1 << ": " << result << endl;
        }
        else {
            currentPoint = 1;
            totalFlips = 0;
          //  cout << s.length() << endl;
            s = getWhatMatters(s);
            while(checkHappiness(s) == false){
               // cout << s << endl;
                s = doMovement(s);
                //cout  << s << endl;
            }
            cout << "Case #" << i+1 << ": " << totalFlips << endl;
        }
    }
}

int workfor2(string s){
    if(s == "+-")
        return 2;
    else if(s == "-+")
        return 1;
    else if(s == "--")
        return 1;
    else
        return 0;
}


bool checkBegin(string s){
    bool minus = false;
    for(long long int i = 0;i < s.length();i++){
        if(s.at(i) == '-')
            minus = true;
    }
    if(minus)
        return true;
    else
        return false;
}

// - + - - - | + +
// - - + + - + - - - | + +
// + + + + - + - - - | + +
// - - - - - + - - - | + +
// + + + + + + - - - | + +
// - - - - - - - - - | + +
// + + + + + + + + + | + +

string getWhatMatters(string input){
    string output = "";
    long long int newPancakeStack;
    for(long long int i = input.length() - 1; i >=0; i--){
        if(input.at(i) == '-'){
            newPancakeStack = i;
            break;
        }
    }
    for(long long int i = 0; i <= newPancakeStack; i++){
        output += input.at(i);
    }
    return output;
}

string doMovement(string pancakeStack){
    string aux= "";
    string rev = "";
    long long int position_to_turn;
    char initial = pancakeStack.at(0);
    bool foundUnequal = false;
    for(long long int i = currentPoint; i < pancakeStack.length(); i++){
        if(pancakeStack.at(i) != initial){
            position_to_turn = i;
            currentPoint = i;
            foundUnequal = true;
            break;

        }
    }
    if(!foundUnequal){
        totalFlips++;
        return "+";
    }
    for(long long int i = position_to_turn-1; i >= 0; i--){
        if(pancakeStack.at(i) == '-')
            aux += "+";
        else
            aux += "-";
    }
    for(long long int i = 0;i< position_to_turn; i++){
        pancakeStack.at(i) = aux.at(i);
    }
    totalFlips++;
    return pancakeStack;
}

bool checkHappiness(string pancakeStack){
    for(long long int i = 0;i < pancakeStack.length(); i++ ){
        if(pancakeStack.at(i) == '-')
            return false;
    }
    return true;
}

bool checkPlus(string s){
    for(int i = 0; i < s.length(); i++){
        if(s.at(i) == '-')
            return false;

    }
    return true;
}

