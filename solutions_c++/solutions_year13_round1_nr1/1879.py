#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

inline int stringToInt(const std::string &fValue)
{
    std::stringstream sstr(fValue);
    int val;
    sstr >> val;
    return val;
}

struct TestCase{
    int r,t;
};

int main()
{
    int numInputs;
    TestCase* inputs;
    int*    outputs;
    // BEGIN - Read file
    std::ifstream inputFile;
    inputFile.open("C:\\Users\\prady\\Downloads\\A-small-attempt0.in");
    if(inputFile.good())
    {
        std::string currentLine;
        std::getline(inputFile,currentLine);
        numInputs	= stringToInt(currentLine);
        inputs		= new TestCase[numInputs];
        outputs     = new int[numInputs];
        currentLine.clear();

        for(int inp=0;inp<numInputs; ++inp) {
            std::getline(inputFile,currentLine);
            stringstream ss(currentLine);
            ss>>inputs[inp].r>>inputs[inp].t;
            currentLine.clear();
        }
    }
    inputFile.close();
    // END - Read file
    for(int inp=0;inp<numInputs;++inp)
    {
        float r = 2*((float)inputs[inp].r)-1;
        float t = ((float)inputs[inp].t);
        outputs[inp] = ((int)((sqrt(r*r+8*t)-r)/4.0));
    }
    //BEGIN - Write to file
    std::ofstream outputFile;
    outputFile.open("output_largeInput.txt");
    if(outputFile.good()) {
        for(int inp=0;inp<numInputs; ++inp) {
            outputFile<<"Case #"<<inp+1<<": "<<outputs[inp]<<std::endl;
        }
    }
    outputFile.close();
    //END - Write to file
    return 0;
}

