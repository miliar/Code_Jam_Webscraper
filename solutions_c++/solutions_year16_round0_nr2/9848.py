#include <iostream>
#include <string>

void flip(std::string s){
    //copying string
    char* stack = new char[s.length()];
    for(int i = 0; i < s.length(); i++){
        if(s[i] == '+') stack[i] = '+';
        else if(s[i] == '-') stack[i] = '-';
    }
    
    int flips = 0;
    
    int deepest = 0;
    while(deepest != -1){
        // finding deepest sad pancake
        deepest = -1;
        for(int i = 0; i < s.length(); i++){
            if(stack[i] == '-') deepest = i;
        }
        for(int i = 0; i <= deepest; i++){
            if(stack[i] == '+') stack[i] = '-';
            else if(stack[i] ==  '-') stack[i] = '+';
        }
        flips++;
    }
    std::cout << flips - 1 << std::endl;
}

int main(){
    // t is number of test cases (one for this problem)
    int t;
    std::string s;
    std::cin >> t;
    for(int i = 0; i < t; i++){
        std::cin >> s;
        std::cout << "Case #" << i + 1 << ": ";
        flip(s);
    }
    return 0;
}