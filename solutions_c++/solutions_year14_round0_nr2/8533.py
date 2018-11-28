#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::stringstream;
using std::string;

//clear the strintstream and get the next line from the input file
void getNextLine (stringstream &theStream, ifstream &input) {
    theStream.clear();
    string theLine;
    getline(input, theLine);
    theStream.str(theLine);
}

int main(int argc, char** argv) {
    char* filename;
    if(argc == 1) {
        cout<<"No input file specified."<<endl;
        return 1;
    } else if (argc > 2) {
        cout<<"Too many arguments"<<endl;
        return 2;
    } else {
        filename = argv[1]; 
    }

    string curLine;
    ifstream inputFile;
    inputFile.open(filename);

    if(!inputFile.is_open()) {
        cout<<"Failed to open file: "<<filename<<endl;
        return 3;
    }

    ofstream outputFile;
    outputFile.open("output", std::ofstream::app);

    int numTests = 0;
    stringstream ss;
    getNextLine(ss, inputFile);
    ss>>numTests;

    if(numTests > 100) {
        cout<<"Too many test cases."<<endl;
        return 4;
    }
    
    double farmCost;
    double ratePerFarm;
    double cookieGoal;
    double timeElapsed;
    double curRate;
    for(int i = 0; i < numTests; ++i) {
        timeElapsed = 0.0;
        curRate = 2.0;
        getNextLine(ss, inputFile);
        ss>>farmCost>>ratePerFarm>>cookieGoal; 
        
        while((cookieGoal/(curRate + ratePerFarm)) < ((cookieGoal - farmCost)/curRate)) {
            timeElapsed += farmCost/curRate;
            curRate += ratePerFarm;
        } 

        timeElapsed += cookieGoal/curRate;
        outputFile<<"Case #"<<(i+1)<<": "<<std::fixed<<std::setprecision(7)<<timeElapsed<<endl;
    }

    return 0;
}
