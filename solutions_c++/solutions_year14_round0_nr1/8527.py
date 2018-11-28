/**
 *  Author: Chris Woyak (AxioM)
 *  
 *  Google Code Jam 2014 Qualifying Round, Problem A
 *  Magic Trick
 */
#include <iostream>
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

int main (int argc, char** argv) {
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

    //declare necessary variables
    int numTests = 0;
    int row1 = 0;
    int row2 = 0;
    int arrangement1[4];
    int arrangement2[4];
    stringstream ss;

    //get the number of test cases to process
    getNextLine(ss, inputFile);
    ss >> numTests;
    
    if(numTests > 100) {
        cout<<"Too many test cases. ("<<numTests<<")"<<endl;
        return 4;
    }

    //do processing...
    for(int i = 0; i < numTests; ++i) {

        getNextLine(ss, inputFile);
        ss>>row1;
        for(int j = 0; j < 4; ++j) {
            getNextLine(ss, inputFile);
            if(j +1 == row1) {
                ss>>arrangement1[0]>>arrangement1[1]>>arrangement1[2]>>arrangement1[3];
            }
        }

        getNextLine(ss, inputFile);
        ss>>row2;
        for(int j = 0; j < 4; ++j) {
            getNextLine(ss, inputFile);
            if(j +1 == row2) {
                ss>>arrangement2[0]>>arrangement2[1]>>arrangement2[2]>>arrangement2[3];
            }
        }

        int count = 0;
        int result;
        for(int j = 0; j < 4; ++j) {
            for(int k = 0; k < 4; ++k) {
                if(arrangement1[j] == arrangement2[k]) {
                    count++;
                    result = arrangement1[j];
                }
            }
        }

        outputFile<<"Case #"<<(i+1)<<": ";
        switch (count) {
            case 1:
                outputFile<<result<<endl; break;
            case 0:
                outputFile<<"Volunteer cheated!"<<endl;   break;
            default:
                outputFile<<"Bad magician!"<<endl;    break;
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
