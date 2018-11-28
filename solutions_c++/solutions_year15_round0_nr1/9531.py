// Google Code Jam 2015 Qualification A

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <cassert>

void jam (std::ifstream&, std::ofstream&);

int main (int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <infile> <outfile>" << std::endl;
        return 1;
    }

    std::string infile, outfile;
    std::stringstream argstream;

    argstream << argv[1];
    argstream >> infile;
    argstream.clear();
    argstream << argv[2];
    argstream >> outfile;
    argstream.clear();

    std::ifstream ifs(infile);
    std::ofstream ofs(outfile);

    jam(ifs, ofs);

    return 0;
}

void jam (std::ifstream& ifs, std::ofstream& ofs) {
    std::string line;
    std::stringstream ss;
    int cases = 0;

    std::getline(ifs, line);
    ss << line;
    ss >> cases;
    ss.clear();

    for (int c = 1; c <= cases; ++c) {
        int maxS = 0;
        std::string shyCount;
        std::vector<int> shyVect;

        std::getline(ifs, line);
        ss << line;
        ss >> maxS;
        ss >> shyCount;
        ss.clear();

        for (char x : shyCount) {
            shyVect.push_back(x - '0');
        }

        // algorithm
        int invites = 0;
        int standing = 0;

        for (int i = 0; i < shyVect.size(); ++i) {
            if (shyVect[i] > 0) {
                if (standing < i) {
                    invites += i - standing;
                    standing = i;
                }

                if (standing >= i) {
                    standing += shyVect[i];
                }
            }
        }

        ofs << "Case #" << c << ": " << invites << std::endl;
    }
}

