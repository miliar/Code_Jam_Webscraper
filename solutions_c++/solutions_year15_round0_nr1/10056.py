#include <string>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

std::vector<std::string> getCrowd(std::string filename);

int main(int argc, char *argv[])
{
    std::vector<std::string> crowd(getCrowd(argv[1]));
    std::ofstream results("results.txt");

    if(results.is_open()) {
        int caseNum = 1;
        int numPpl, pos, pplNeeded, diff;
        for(std::string s : crowd) {
            numPpl = pos = pplNeeded = 0;
            int length = s.length();

            for(unsigned int i = 0; i < length + 1; ++i) {
                if(numPpl < i) {
                    diff = i - numPpl;
                } else {
                    diff = 0;
                }

                pplNeeded += diff;
                numPpl += diff;
                char tmp = s[i];
                numPpl += (i == s.length()) ? 0 : atoi(&tmp);
            }

            results << "Case #" << caseNum << ": " << pplNeeded << "\n";
            ++caseNum;
        }

    } else {
        std::cerr << "ERROR: unable to open out file" << std::endl;
        exit(-1);
    }

    return 0;
}

std::vector<std::string> getCrowd(std::string filename)
{
    std::string line;
    std::ifstream file(filename.c_str());
    std::vector<std::string> crowd;

    int count = 0;
    if(file.is_open()) {
        while(std::getline(file, line)) {
            if(count)
                crowd.push_back(line.substr(line.find_first_of(" ") + 1));
            ++count;
        }
    } else {
        std::cerr << "ERROR: unable to open in file" << std::endl;
        exit(-1);
    }

    file.close();
    return crowd;
}
