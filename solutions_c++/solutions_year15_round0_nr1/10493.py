#include <iostream>
#include <vector>
#include <cstdlib> //atoi()
using namespace std;


int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int j = 0; j < T; ++j) {
        int Smax;
        cin >> Smax;
        //cout << Smax << endl;
        int currentStanding = 0;
        int friends = 0;
        string guests;
        cin >> guests;
        for (int i = 0; i < guests.size(); ++i) {
            char current = guests.at(i);
            int guestsWithSi = atoi(&current);
            //cout << guestsWithSi;
            if (i > currentStanding) {
                friends += (i - currentStanding);
                currentStanding += (i - currentStanding);
            }
            currentStanding += guestsWithSi;
        }
        //cout << endl;

        cout << "Case #" << j + 1  << ": " << friends << endl;
    }
}
