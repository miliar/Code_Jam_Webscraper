#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <stdexcept>

using namespace std;

bool isNumber(const std::string& s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) {
        it++;
    }
    return !s.empty() && it == s.end();
}

int stringToInteger(const string &str) {
    stringstream ss(str);
    int num;
    if((ss >> num).fail())
    {
        throw new runtime_error("Error - input string: " + str);
    }
    return num;
}

string integerToString(int number) {
    ostringstream ss;
    ss << number;
    return ss.str();
}

vector<int> transformStringToIntVector(string line) {
    vector<int> intVector;

    istringstream lineStream(line);
    string token;

    while (lineStream >> token) {
        intVector.push_back(stringToInteger(token));
    }

    return intVector;
}

vector<int> findMatchesInIntVector(vector<int> a, vector<int> b) {
    vector<int> matches;

    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < b.size(); j++) {
            if (a[i] == b[j]) {
                matches.push_back(a[i]);
            }
        }
    }

    return matches;
}

void solveForMatchingNumberInLines(int caseNumber, string a, string b) {
    vector<int> vectorA = transformStringToIntVector(a);
    vector<int> vectorB = transformStringToIntVector(b);

    vector<int> matches = findMatchesInIntVector(vectorA, vectorB);

    cout << "Case #" << caseNumber << ": ";
    if (matches.size() == 0) {
        cout << "Volunteer cheated!" << endl;
    } else if (matches.size() == 1) {
        cout << matches[0] << endl;
    } else {
        cout << "Bad magician!" << endl;
    }
}

class GCJ1 {

public:
    void Solve();
};

void GCJ1::Solve() {
    vector<string> inputStream;
    string line;

    getline(cin, line);
    int numberOfCases = stringToInteger(line);

    while (getline(cin, line)) {
        inputStream.push_back(line);
    }

    for (int n = 0; n < numberOfCases; ++n) {
        int answer1;
        int answer2;
        string answerLine1;
        string answerLine2;

        answer1 = stringToInteger(inputStream[n * 10]);
        answer2 = stringToInteger(inputStream[n * 10 + 5]);

        answerLine1 = inputStream[n * 10 + answer1];
        answerLine2 = inputStream[n * 10 + 5 + answer2];

        solveForMatchingNumberInLines(n + 1, answerLine1, answerLine2);
    }
}

int main(int argc, char const *argv[])
{
    GCJ1* question = new GCJ1();
    question->Solve();
    return 0;
}
