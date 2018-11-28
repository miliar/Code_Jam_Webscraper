#include <iostream>
#include <string>
#include <sstream>

using namespace std;
string flip(string stack){
    for(size_t i = 0; i < stack.length(); i++){
        stack[i] = stack[i] == '+' ? '-' : '+';
    }
    return stack;
}
int flipCakes(int num_flips, string stack){
    if(stack.length() == 0) return num_flips;
    
    string rest = stack.substr(0, stack.length() - 1);
    if(stack[stack.length() - 1] == '+'){
        return flipCakes(num_flips, rest);    
    }else{
        string flipped = flip(rest);
        return flipCakes(num_flips + 1, flipped);
    }
    return 100;
}

int main(){
    int num_input = 0;
    string temp;
    getline(cin, temp);
    istringstream iss(temp);
    iss >> num_input;
    for(int i = 0; i < num_input; i++){
        getline(cin, temp);
        cout << "Case #" << i+1 << ": " << flipCakes(0, temp) << endl;
    }
    return 0;
}
