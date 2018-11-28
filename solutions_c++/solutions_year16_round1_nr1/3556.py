#include <iostream>
#include <fstream>
#include <string>



using namespace std;

string solveCase(string);
int main() {


    string inputFileName;
    string outputFileName;
    cout<<"Enter input file name: ";
    cin>>inputFileName;
    cout<<"Enter output file name: ";
    cin>>outputFileName;

    ifstream fInput(inputFileName, ios::in);
    ofstream fOutput(outputFileName, ios::out);

    unsigned cases;
    string phrase;
    string lastWord;

    fInput>>cases; // read in # of cases


    for(unsigned count = 0; count < cases; count++) {
        fInput>>phrase; //hold the case
        cout<<phrase;
        lastWord = solveCase(phrase);
        fOutput<<"Case #"<<count + 1<<": "<<lastWord<<endl;
    }

}

string solveCase(string phrase) {
    string result = "";
    result = result + phrase[0]; //set it to the first char
    string tmp1; //in front
    string tmp2; // in back
    for(unsigned count = 1; count < phrase.size(); count++) {
        tmp1 = phrase[count] + result;
        tmp2 = result + phrase[count];
        if(tmp1 > tmp2)
            result = tmp1;
        else
            result = tmp2;
    }
    return result;

}