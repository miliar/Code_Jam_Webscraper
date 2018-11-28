#include "junction.h"
#include <string>
#include <algorithm>

void pancakes (){
    int T, found, steps;
    string pancake_stack ("");

    cin >> T;

    for (int i=0; i<T; i++){
        cin >> pancake_stack;
        steps=0;
        while (pancake_stack.size() != 0){

//Deletes group of plusses from the end
            while (pancake_stack[pancake_stack.size()-1] == '+'){
                pancake_stack = pancake_stack.substr(0, pancake_stack.size()-1);
            }

            if (pancake_stack.size() == 0) break;

//munchy algorithm is here
//flip rightmost +
            if (pancake_stack[0] != '-' || pancake_stack[pancake_stack.size()-1] != '-'){
                steps ++;
                found = pancake_stack.find_last_of('+');
                reverse(pancake_stack.begin(), pancake_stack.begin()+found+1);

                for (int j=0; j<found+1; j++){
                    if (pancake_stack[j]=='+') pancake_stack[j]='-';
                    else pancake_stack[j]='+';
                }
 //               cout << "current stack: " << pancake_stack << endl;
            }
//front and back is "-" flip
            else if (pancake_stack[0] == '-' && pancake_stack[pancake_stack.size()-1] == '-') {
                steps ++;
                reverse(pancake_stack.begin(), pancake_stack.end());
                    for (int j=0; j<pancake_stack.size(); j++){
                        if (pancake_stack[j]=='+') pancake_stack[j]='-';
                        else pancake_stack[j]='+';
                }
 //               cout << "current stack: " << pancake_stack << endl;
            }
            //Deletes group of plusses from the end
            while (pancake_stack[pancake_stack.size()-1] == '+'){
                pancake_stack = pancake_stack.substr(0, pancake_stack.size()-1);
            }
        }
        cout << "Case #" << i+1 << ": " << steps << endl;

    }
}

