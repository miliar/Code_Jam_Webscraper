#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int t;
    cin >> t;
    string line;
    getline(cin, line);
    for (int round = 1; round <= t; ++round) {
        string output;
        getline(cin, line);

        istringstream iss(line);
        char ch;
        while(iss >> ch) {
            string tmp(&ch);
            if (ch >= *(output.begin())) {
                output = tmp + output;
            } else {
                output = output + tmp;
            }
//            cout << output << endl;
        }

        cout << "Case #" << round << ": " << output << endl;
    }
return 0;
}
