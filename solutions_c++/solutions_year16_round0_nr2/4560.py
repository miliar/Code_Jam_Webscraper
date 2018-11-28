#include <bits/stdc++.h>

using namespace std;

int main( )
{
    string actual;
    int T, flips; 
    char last;

    cin >> T;
    for(int i = 1; i <= T; ++i) 
    {
        flips = 0;
        cin >> actual;
        last = actual[0];

        for(int j = 1; actual[j] != '\0'; ++j) {
            if(actual[j] != last) {
                ++flips;
                last = actual[j];
            }

        }
        if(last == '-') ++flips;

        cout << "Case #" << i <<": " << flips << endl;

    }


    return 0;

}