#include <iostream>
#include <fstream>
#include <string>

const std::string inFileName = "A-large.in";
const std::string outFileName = "lastWordLargeOUT.txt";


std::string lastWord(const std::string& s);



int main() {

    std::ifstream inFile(inFileName);
    std::ofstream outFile(outFileName);

    std::string s;



    unsigned T;
    inFile >> T;

    for (unsigned i = 1; i <= T; i++) {

        inFile >> s;

        outFile << "Case #" << i << ": " << lastWord(s) << std::endl;
    }




    return 0;
}

std::string lastWord(const std::string& s) {
    std::string lWord = s.substr(0, 1);

    //iterate through rest
    for (unsigned i = 1; i < s.size(); ++i) {
        
        if(s[i] >= lWord[0]) {
            lWord = s[i] + lWord;
        }
        else {
            lWord = lWord + s[i];
        }
    }

    return lWord;
}