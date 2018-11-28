#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

unsigned reqFlips(string);
bool allHappy(string);
void flip(string &);
int main() {
    string inputFileName;
    string outputFileName;

    cout<<"Enter input file name: ";
    cin>>inputFileName;
    cout<<"Enter output file name: ";
    cin>>outputFileName;

    ifstream fInput(inputFileName, ios::in);
    ofstream fOutput(outputFileName, ios::out);

    string tmpPancakes;
    vector<string> pancakeStacks;
    unsigned numStacks;

    fInput>>numStacks;
    for(unsigned count = 0; count < numStacks; count++) {
        fInput>>tmpPancakes;
        pancakeStacks.push_back(tmpPancakes);
    }
    /*for(unsigned count = 0; count < numStacks; count++)
        cout<<pancakeStacks[count]<<endl;*/

    for(unsigned count = 0; count < numStacks; count++) {
        fOutput<<"Case #"<<count + 1<<": "<<reqFlips(pancakeStacks[count])
               <<endl;
    }

}

unsigned reqFlips(string pancakes) {
    unsigned numFlips = 0;
    while(true) {
        if(allHappy(pancakes))
            break;
        flip(pancakes);
        ++numFlips;
    }
    return numFlips;
}

bool allHappy(string checkedPancakes) {
    bool returnValue = true;
    for(unsigned count = 0; count < checkedPancakes.size(); count++) {
        if(checkedPancakes[count] == '-') {
            returnValue = false;
            break;
        }
    }
    return returnValue;
}

void flip(string & pancakesToFlip) {
    char topPancake = pancakesToFlip[0];
    char otherSide;
    if(topPancake == '+')
        otherSide = '-';
    else
        otherSide = '+';

    unsigned index; 
    for(index = 0; index < pancakesToFlip.size(); index++) {
        if(pancakesToFlip[index] != topPancake) {
            ++index;
            break;
        }
    }
    for(unsigned count = 0; count < index; count++)
        pancakesToFlip[count] = otherSide;
}