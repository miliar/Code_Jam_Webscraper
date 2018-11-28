#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <stdexcept>
#include <cstdio>

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

vector<double> transformStringToDoubleVector(string line) {
    vector<double> doubleVector;

    istringstream lineStream(line);
    double token;

    while (lineStream >> token) {
        doubleVector.push_back(token);
    }

    return doubleVector;
}

class GCJ2 {
    vector<double> runTimes;
    void Solve(int caseNumber, double currentRunTime, double production, double C, double F, double X);
public:
    void Solve();
};

void GCJ2::Solve(int caseNumber, double currentRunTime, double production, double C, double F, double X) {
    double doNotBuyFarmTime = X / production;
    runTimes.push_back(currentRunTime + doNotBuyFarmTime);

    if (doNotBuyFarmTime < 0.1) {
        return;
    }

    double newFarmTime = C / production;
    Solve(caseNumber, currentRunTime + newFarmTime, production + F, C, F, X);
}

void GCJ2::Solve() {
    vector<string> inputStream;
    string line;

    getline(cin, line);
    int numberOfCases = stringToInteger(line);

    while (getline(cin, line)) {
        inputStream.push_back(line);
    }

    for (int n = 0; n < numberOfCases; ++n) {
        vector<double> testCase = transformStringToDoubleVector(inputStream[n]);

        Solve(n+1, 0, 2.0000000, testCase[0], testCase[1], testCase[2]);

        double minimumTime = runTimes[0];
        for (int i = 1; i < runTimes.size(); ++i) {
            if (minimumTime > runTimes[i]) {
                minimumTime = runTimes[i];
            }
        }
        this->runTimes.clear();
        printf("Case #%d: %0.7f", n + 1,  minimumTime);
        cout << endl;
    }
}

int main(int argc, char const *argv[])
{
    GCJ2* question = new GCJ2();
    question->Solve();
    return 0;
}
