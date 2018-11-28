#include <iostream>
#include <fstream>

#include <vector>
#include <math.h>

using namespace std;

void printBoolArray(bool []);

int main(){
    ofstream outputFile ("output.txt");
    ifstream inputFile ("B-large.in");
    string line;
    int stacksCount;

    inputFile >> stacksCount;
    getline(inputFile, line);

    for(int s = 0; s < stacksCount; s++){
        getline(inputFile, line);
        bool stack[line.length()];

        // Populate original stack
        for(int si = 0; si < line.length(); si++){
            char currSymbol = line[si];

            if(currSymbol == '-'){
                stack[si] = false;
            }else{
                stack[si] = true;
            }
        }

        // Stackerinate
        int swapCount = 0;
        bool done = false;

        while(!done){

            // Check Goodness
            int goodness = 0;
            for(int x = 0; x < sizeof(stack); x++){
                if(stack[x])
                    goodness += 1;
            }
            if(goodness == sizeof(stack)){
                done = true;
                break;
            }

            // If not good, flip baby

            int lastLocationIndex = sizeof(stack) - 1;
            int lastLocation = stack[lastLocationIndex];

            while(lastLocation){
                lastLocationIndex -= 1;

                lastLocation = stack[lastLocationIndex];
            }

            if(lastLocationIndex < 0)
                lastLocationIndex = sizeof(stack) - 1;

            for(int i = 0; i <= lastLocationIndex; i++){
                stack[i] = !stack[i]; // flip flip flippity flip
            }

            // Print out
            cout << "lastLocation: " << lastLocationIndex << "\n";

            for(int x = 0; x < sizeof(stack); x++){
                if(stack[x]){
                    cout << "+";
                }else{
                    cout << "-";
                }
            }

            cout << "\n";

            swapCount += 1;
            //break;
        }

        cout << "Total Swaps: " << swapCount << "\n";
        outputFile << "Case #" << (s + 1) << ": " << swapCount << "\n";
    }

    outputFile.close();
    inputFile.close();
}
