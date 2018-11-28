#include <iostream>
#include <c++/fstream>
#include <c++/sstream>

using namespace std;

inline unsigned int numberOfFlips(unsigned int alternatingPiles, bool startsWithSmileUp) {
    if(startsWithSmileUp == (alternatingPiles % 2 == 0))
        return alternatingPiles;
    else
        return alternatingPiles - 1;
}

int main() {
    ofstream ofs("output.txt");
    ifstream fs("input.txt");
    cout << "Hello, World!" << endl;

    string line;
    bool startsWithSmileUp;
    unsigned int numberOfPilesOfConsecutiveCookieOrientation = 1;
    ostringstream outline;

    std::getline(fs, line); // consumes number.

    string emptyStr = "";
    char searchedCharacter;
    for (unsigned int i = 1, line_index = 0; std::getline(fs, line);
         ++i, line_index = 0,
         numberOfPilesOfConsecutiveCookieOrientation = 1,
         outline.str(emptyStr))
    {
        cout << line << endl;

        if(line.size() == 0) {
            cout << "WTF no cookies !";
            return -1;
        }

        searchedCharacter = line[0];
        startsWithSmileUp = searchedCharacter == '+';


        for(; line_index < line.size() ; ++line_index) {
            switch (line[line_index]) {
                case '+' : {
                    if (searchedCharacter == '-') {
                        searchedCharacter = '+';
                        ++numberOfPilesOfConsecutiveCookieOrientation;

                    }
                    break;
                }
                case '-' : {
                    if (searchedCharacter == '+') {
                        searchedCharacter = '-';
                        ++numberOfPilesOfConsecutiveCookieOrientation;
                    }
                    break;
                }
                default: {
                    cout << "WTF weird '" << line[line_index] << "' !";
                    return -2;
                }
            }
        } // line loop

        outline << "Case #" << i << ": "
                << numberOfFlips(numberOfPilesOfConsecutiveCookieOrientation, startsWithSmileUp)
                << endl;
        outline.flush();

        cout << outline.str();
        ofs << outline.str();
    }

    fs.close();
    ofs.close();

    return 0;
}