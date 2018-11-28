#include <iostream>
#include <string>
#define TRUE 1
#define FALSE 0

using namespace std;

int flipPancakes (string pancakeStack);
int allPancakesHappy (string pancakeStack);
string flipFromLastMinus (string pancakeStack);
int lastMinusIndex (string pancakeStack);

int main(int argc, char ** argv) {
    int testCases, testCaseCounter;

    cin >> testCases;
    for (testCaseCounter = 0; testCaseCounter < testCases; testCaseCounter ++){
        string pancakeStack = "Hello";
        cin >> pancakeStack;

        int numberOfFlips = flipPancakes(pancakeStack);

        cout << "Case #" << testCaseCounter + 1 << ": " << numberOfFlips << endl;
    }
    return EXIT_SUCCESS;
}

int flipPancakes (string pancakeStack){
    int numberOfFlips = 0;
    while (allPancakesHappy(pancakeStack) == FALSE){
        pancakeStack = flipFromLastMinus(pancakeStack);
        numberOfFlips ++;
    }
    return numberOfFlips;
}

int allPancakesHappy (string pancakeStack){
    int result = FALSE;
    int stringIndex;
    int countHappyPancakes = 0;
    for (stringIndex = 0; stringIndex < pancakeStack.length(); stringIndex ++){
        if (pancakeStack[stringIndex] == '+'){
            countHappyPancakes ++;
        }
    }
    if (countHappyPancakes == pancakeStack.length()){
        result = TRUE;
    }
    return result;
}

string flipFromLastMinus (string pancakeStack){
    int flipFromIndex = lastMinusIndex(pancakeStack);
    for (flipFromIndex; flipFromIndex >= 0; flipFromIndex --){
        if (pancakeStack[flipFromIndex] == '-'){
            pancakeStack[flipFromIndex] = '+';
        } else if (pancakeStack[flipFromIndex] == '+'){
            pancakeStack[flipFromIndex] = '-';
        }
    }
    return pancakeStack;
}

int lastMinusIndex (string pancakeStack){
    int lastIndex = pancakeStack.length()-1;
    while (pancakeStack[lastIndex] == '+'){
        lastIndex --;
    }
    return lastIndex;
}


