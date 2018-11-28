#include <iostream>
#include <set>

using namespace std;

int main()
{
    int numCases;
    int N;

    cin >> numCases;

    for (int i = 0; i < numCases; ++i) {
        long factor = 0;
        long name = 0;
        set<char> seenNumbers {};
        set<char> allNumbers {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

        cin >> N;

        if (N != 0) {
            //cout << "N: " << N << endl;

            while (seenNumbers != allNumbers) {
                factor++;
                // Calc
                name = factor * N;
                //cout << "name: " << name << endl;

                // To string
                string nameStr = to_string(name);

                // Compare character by character
                for (int j = 0; j < nameStr.length(); ++j) {
                    auto found = seenNumbers.find(nameStr[j]);
                    if (found == seenNumbers.end()) {
                        seenNumbers.insert(nameStr[j]);
                    }
                }
            }
        }

        if (factor != 0)
            cout << "Case #" << i + 1 << ": " << name << endl;
        else
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
    }

    return 0;
}

