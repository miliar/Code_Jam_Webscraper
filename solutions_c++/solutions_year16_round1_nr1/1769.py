/*
Will Long
Google Code Jam 2016
Round 1A - Problem 1

April 15, 2016
*/

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, const char *argv[])
{
    string fname = argv[1];
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);

    int cases;
    cin >> cases;

    string S, result;
    for (int i = 1; i <= cases; i++) {
        cin >> S;
        result = S.substr(0, 1);
        for (int j = 1; j < S.length(); j++) {
            if (S.at(j) >= result.at(0)) {
                result = S.at(j) + result;
            } else {
                result += S.at(j);
            }
        }
        cout << "Case #" << i << ": " << result << endl;
    }

    return 0;
}