#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

// create audience class
class Audience {
    private:
        std::vector<unsigned> shyness;
        int index;
        int sum;
    public:
        unsigned getMaxShyness(){
            return shyness.size() - 1;
        }
        Audience(std::string& shyness){
            for (std::string::const_iterator i = shyness.cbegin(); i != shyness.cend(); ++i)
                this->shyness.push_back(*i - '0');
            this->index = -1;
            this-> sum = 0;
        }
        int nextMismatch(){
            for (int i = index + 1; i < shyness.size(); ++i) {
                sum += shyness[i];
                if (sum <= i) {
                    index = i;
                    ++sum;
                    return index;
                }
            }
            return -1;
        }
        void reset() {
            sum = 0;
            index = -1;
        }
};

// read the test case file
std::vector<Audience> readTC(const std::string& inputFile) {
    std::ifstream myfile(inputFile.c_str(), std::ios::in);
    std::vector<Audience> audience;
    if (myfile.is_open()) {
        std::string line;
        bool first = true;
        unsigned numCases = 0;
        while(std::getline(myfile, line)) {
            if (first) {
                numCases = std::stoi(line.c_str());
                first = false;
                continue;
            }
            std::stringstream sstr(line);
            std::string first;
            std::string second;
            sstr >> first >> second;
            Audience aud(second);
            audience.push_back(aud);
        }
    }
    return audience;
}

int main () {
    std::string file("/Users/skarunakaran/cj/TC.txt");
    std::vector<Audience> auds = readTC(file);
    int count = 0;
    for (std::vector<Audience>::iterator i = auds.begin(); i != auds.end(); ++i) {
        unsigned mismatch = 0;
        while (i->nextMismatch() >= 0) {
            ++mismatch;
        }
	count++;
        std::cout << "Case #" << count << ": " << mismatch << std::endl;
    }
    return 0;
}
