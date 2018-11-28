#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

vector<unsigned> values;
unsigned cases;

void extractValues();
int getResult(unsigned);
int main() {
    const string outputFileName = "counting_sheep_output.txt";
    ofstream fOutput(outputFileName, ios::out);
    int tmpResult;

    extractValues();

    for(unsigned count = 0; count < cases; count++) {
        tmpResult = getResult(count);
        fOutput<<"Case #"<<count + 1<<": ";
        if(tmpResult != -1) 
            fOutput<<tmpResult<<'\n';
        else
            fOutput<<"INSOMNIA"<<'\n';
    }
    return 0;
}

void extractValues() {
    string inputFileName;
    unsigned tmpValue;

    cout<<"Enter file name: ";
    cin>>inputFileName;

    ifstream fInput(inputFileName, ios::in);

    fInput>>cases;
    for(unsigned count = 0; count < cases; count++) {
        fInput>>tmpValue;
        values.push_back(tmpValue);
    }
    /*for(unsigned count = 0; count < cases; count++) {
        cout<<values[count]<<endl;
    }*/

}
bool allDigitsAccounted(bool[]);
int getResult(unsigned caseNum) {
    double value = values[caseNum];
    const unsigned numDigits = 10;
    unsigned extractedDigit;
    bool digits[numDigits];


    for(unsigned count = 0; count < numDigits; count++)
        digits[count] = false;

    int iteration = 1;
    int multiple;
    int hold;

    while(true) {
        multiple = iteration * value;
        if(multiple <= 0)
            return -1;
        hold = multiple;

        while(hold > 0) {
            extractedDigit = hold % numDigits;
            hold = (hold - extractedDigit) / numDigits;
            digits[extractedDigit] = true;
        }
        if(allDigitsAccounted(digits))
            return multiple;
        ++iteration;
    }

}
bool allDigitsAccounted(bool tmpArray[]) {
    bool returnValue = true;
    const unsigned numDigits = 10;
    for(unsigned count = 0; count < numDigits; count++) {
        if(!tmpArray[count]) {
            returnValue = false;
            break;
        }
    }
    return returnValue;
}