#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>

const std::string inFileName = "B-large.in";
const std::string outFileName = "pancakesOUT.txt";


unsigned numSwaps(std::vector<bool>& v);
void flip(std::vector<bool>& v, unsigned first, unsigned last); //flip from first to last
void disp(std::vector<bool>& v);
void convertToBitVec(std::string& s, std::vector<bool>& v);



void convertToBitVec(std::string& s, std::vector<bool>& v) {
    for (unsigned i = 0; i < s.length(); ++i) {
        v[i] = (s[i] == '+')? true : false;
    }
}


int main() {

    std::ifstream inFile(inFileName);
    std::ofstream outFile(outFileName);

    std::string s;
    std::vector<bool> v;



    unsigned T;
    inFile >> T;

    for (unsigned i = 1; i <= T; i++) {

        inFile >> s;
        v.resize(s.length());
        convertToBitVec(s, v);
        outFile << "Case #" << i << ": " << numSwaps(v) << std::endl;
    }




    return 0;
}

unsigned numSwaps(std::vector<bool>& v) {

    unsigned num = 0;

    for (unsigned i = v.size()-1; i >= 0 && i < v.size(); --i) { //iterate from end

        if(!v[i]) { //if v[i] is 0
            flip(v, 0, i);
            num += 1;
        }
    }

    return num;
}


void flip(std::vector<bool>& v, unsigned first, unsigned last) {

    for (unsigned i = first; i <= last; ++i) {

        v[i] = !v[i];
    }
}

void disp(std::vector<bool>& v) {

    std::cout << "\n(";

    for(bool b : v) {
        std::cout << " " << b << " ";
    }

    std::cout << ")" << std::endl;
}
