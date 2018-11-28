#include <iostream>
#include <string>
#include <set>

using namespace std;

void printSheepSolution(long long N) {
    // 0 <= N <= 1e6
    if(N == 0) {
        cout << "INSOMNIA";
    } else {
        set<char> seenDigits;
        auto seeNumber = [&seenDigits](long long v) {
            set<char> digits;
            string digitString = to_string(v);
            seenDigits.insert(digitString.begin(), digitString.end());
        };

        for(long long i = 1; ; i++) {
            seeNumber(i * N);
            if(seenDigits.size() == 10) {
                cout << i * N;
                return;
            }
        }

        cout << "TIMEOUT!";
    }
}

int main() {
    int numCases;
    cin >> numCases;
    
    for(int caseNum = 1; caseNum <= numCases; ++caseNum) {
        cout << "Case #" << caseNum << ": ";

        long long N;
        cin >> N;
        printSheepSolution(N);

        cout << endl;
    }
}
