#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main(int argc, char** argv)
{
    int tests;
    cin >> tests;
    string blank;
    getline(cin, blank);

    vector<vector<pair<char,int> > > strings;

    for (int t = 1; t <= tests; t++)
    {
        // Handle Case #t
        int n;
        cin >> n;
        getline(cin, blank);

        strings.clear();
        for (int s = 1; s <= n; s++) {
            char string[150];
            for ( int b = 0 ; b < 150 ; b++) {
                string[b] = 0;
            }
            cin.getline(string, 150);

            vector<pair<char,int> > oneString;
            int number = 0;
            char lastChar = 0;
            for (int c = 0; c < 100 && string[c] != 0; c++) {
                if ( lastChar == 0 ) {
                    lastChar = string[c];
                } else if ( lastChar != string[c] ) {
                    oneString.push_back(pair<char,int>(lastChar, number));
                    lastChar = string[c];
                    number = 0;
                }
                number++;
            }
            if ( lastChar != 0 ) {
                oneString.push_back(pair<char,int>(lastChar, number));
            }
            strings.push_back(oneString);
        }

        bool impossible = false;
        int size = 0;
        for (int s = 0; s < n; s++) {
            if ( size == 0 ) {
                size = strings.at(s).size();
            } else if ( size != strings.at(s).size() ) {
                impossible = true;
                break;
            }
        }

        int changes = 0;
        if ( !impossible ) {
            for (int c = 0; c < strings.at(0).size(); c++) {
                int number = 0;
                char lastChar = 0;
                for (int s = 0; s < n; s++) {
                    if ( lastChar == 0 ) {
                        lastChar = strings.at(s).at(c).first;
                        number += strings.at(s).at(c).second;
                    } else if ( lastChar != strings.at(s).at(c).first ) {
                        impossible = true;
                        break;
                    } else {
                        number += strings.at(s).at(c).second;
                    }

                }
                if ( impossible ) break;

                int average = number / n;
                for (int s = 0; s < n; s++) {
                    int diff = strings.at(s).at(c).second - average;
                    changes += diff < 0 ? -diff : diff;
                }
            }

        }

        // Print result for Case #t
        cout << "Case #" << t << ": ";
        if ( impossible ) {
            cout << "Fegla Won";
        } else {
            cout << changes;
        }
        cout << "\n";
    }

    return 0;
}

