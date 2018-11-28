#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    //Get test cases
    int T;
    cin >>T;
    
    string line;
    stringstream ss;
    int Smax;
    string audience;
    int clapping;
    int neededGuests;
    
    //past line
    getline(cin, line);
    //get and analyze case
    for (int t = 0; t < T; t++) {
        clapping = 0;
        neededGuests = 0;
        
        getline(cin, line);
        ss << line;
        ss >> Smax;
        ss >> audience;
        for (int s = 0; s <= Smax; s++) {
            if (s <= clapping) clapping += (int)audience[s] - 48;
            else {
                neededGuests += (s - clapping);
                clapping += (s - clapping) + ((int)audience[s] - 48);
            }
        }
        ss.clear();
        cout <<"Case #" <<t+1 <<": " <<neededGuests <<endl;
    }
}
