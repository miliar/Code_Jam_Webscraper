#include <deque>
#include <iostream>
#include <string>
#include <sstream>
#include <stdexcept>
#include <cstdio>

#include <algorithm>

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

deque<double> getDoubleVectorFromString(string s) {
    deque<double> doubleVector;

    istringstream doubleStream(s);
    double token;

    while (doubleStream >> token) {
        doubleVector.push_back(token);
    }

    return doubleVector;
}

class GCJ4 {
public:
    void Solve();
};

class Game {
    int numberOfBlocks;
    deque<double> nBlocks;
    deque<double> kBlocks;
public:
    int normalScore;
    int deceitScore;

    Game(int n, deque<double> nBlocks, deque<double> kBlocks);
    void SolveDeceit();
    void SolveNormal();
};

Game::Game(int n, deque<double> nBlocks, deque<double> kBlocks) {
    numberOfBlocks = n;

    sort(nBlocks.begin(), nBlocks.end());
    sort(kBlocks.begin(), kBlocks.end());

    this->nBlocks = nBlocks;
    this->kBlocks = kBlocks;
}

void Game::SolveNormal() {
    deque<double> nQueue(nBlocks.begin(), nBlocks.end());
    deque<double> kQueue(kBlocks.begin(), kBlocks.end());

    int naomiScore = 0;
    int kenScore = 0;

    int nValue = nQueue.back();
    int kValue = kQueue.back();

    int n = numberOfBlocks - 1;
    int k = numberOfBlocks - 1;

    while (nQueue.size() > 0 && kQueue.size() > 0) {

        if (nQueue[n] > kQueue[k]) {
            nQueue.pop_back();
            kQueue.pop_front();
            naomiScore++;

        } else {
            nQueue.pop_back();
            kQueue.pop_back();
            kenScore++;
        }

        n--;
        k--;
    }

    normalScore = naomiScore;
}

void Game::SolveDeceit() {
    deque<double> nQueue(nBlocks.begin(), nBlocks.end());
    deque<double> kQueue(kBlocks.begin(), kBlocks.end());

    int naomiScore = 0;
    int kenScore = 0;

    // for (int i = 0; i < nQueue.size(); i++) {
    //     cout << nQueue[i] << " ";
    // }
    // cout << endl;
    // for (int i = 0; i < kQueue.size(); i++) {
    //     cout << kQueue[i] << " ";
    // }
    // cout << endl;

    int i = 0;
    int n = nQueue.size() - 1;
    int k = kQueue.size() - 1;

    while (i < numberOfBlocks) {
        if (nQueue.front() < kQueue.front()) {
            nQueue.pop_front();
            kQueue.pop_back();

            kenScore++;
        } else {
            nQueue.pop_front();
            kQueue.pop_front();

            naomiScore++;
        }

        i++;
    }

    deceitScore = naomiScore;
}

void GCJ4::Solve() {
    deque<string> inputStream;
    string line;

    getline(cin, line);
    int numberOfCases = stringToInteger(line);

    while (getline(cin, line)) {
        inputStream.push_back(line);
    }

    for (int n = 0; n < numberOfCases; ++n) {
        int cases = stringToInteger(inputStream[3 * n]);
        deque<double> nVector = getDoubleVectorFromString(inputStream[3 * n + 1]);
        deque<double> kVector = getDoubleVectorFromString(inputStream[3 * n + 2]);

        Game* game = new Game(cases, nVector, kVector);
        game->SolveNormal();
        game->SolveDeceit();

        cout << "Case #" << n + 1 << ": " << game->deceitScore << " " << game->normalScore << endl;

        delete game;
    }
}

int main(int argc, char const *argv[])
{
    GCJ4* question = new GCJ4();
    question->Solve();
    return 0;
}
