#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void print(const vector<string>& v) {
    for (int i = 0; i < v.size(); ++i) {
        cout << v[i] << endl;
    }
    cout << endl;
}

bool isConsonant(char c) {
    return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int substrings(string s, int minNumConsonants) {
    int nValue = 0;
    vector<string> validSubstrings;

    for (int charPos = 0; charPos < s.length() - minNumConsonants + 1; ++charPos) {
        for (int stringLength = minNumConsonants; stringLength < s.length() - charPos + 1; ++stringLength) {
            validSubstrings.push_back(s.substr(charPos, stringLength));
        }
    }

//    print(validSubstrings);

    for (int i = 0; i < validSubstrings.size(); ++i) {
        string s = validSubstrings[i];
        bool previousCharWasConsonant = false;
        int consecutiveConsonantCounter = 0;
        int maxNumConsonants = 0;

        for (int pos = 0; pos < s.size(); ++pos) {
            if(isConsonant(s[pos])) {
//                cout << "Char " << s[pos] << " is consonant." << endl;
                if (previousCharWasConsonant) {
                    ++consecutiveConsonantCounter;
                } else {
                    consecutiveConsonantCounter = 1;
                }
                maxNumConsonants = max(maxNumConsonants, consecutiveConsonantCounter);
                previousCharWasConsonant = true;
            } else {
                previousCharWasConsonant = false;
            }
        }

//        cout << maxNumConsonants << endl;

        if (maxNumConsonants >= minNumConsonants) {
            ++nValue;
        }
    }

    return nValue;
}

int main()
{
    ifstream inStream("A-small-attempt1.in");
//    ostream& outStream = cout;
    ofstream outStream("A-small-attempt1.out");

    int numCases;
    inStream >> numCases;

    for (int i = 1; i <= numCases; ++i) {
        string name;
        int minNumConsonants;

        inStream >> name;
        inStream >> minNumConsonants;

        cout << name << " ";
        cout << minNumConsonants << endl;

        int solution = substrings(name, minNumConsonants);
        outStream << "Case #" << i << ": " << solution << endl;
    }

    inStream.close();
    outStream.close();

    return 0;
}
