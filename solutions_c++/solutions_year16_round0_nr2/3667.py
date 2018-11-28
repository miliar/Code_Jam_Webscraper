#include <iostream>
#include <fstream>
using namespace std;

int solve(const string& pancakes)
{
    int result = 0;
    char lastPancake = pancakes[0];
    for (int i=1; i<pancakes.length(); ++i)
    {
        if (lastPancake != pancakes[i]) {
            ++result;
            lastPancake = pancakes[i];
        }
    }
    if (lastPancake == '-') {
        ++result;
    }
    return result;
}

int main()
{
    int nCases;
    cin >> nCases;
    cin.ignore (1, '\n');
    for (int i=0; i<nCases; ++i) {
        string input;
        getline(cin, input);
        int result = solve(input);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}
