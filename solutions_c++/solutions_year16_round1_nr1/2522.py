
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main ()
{
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        string word, result;
        cin >> word;

        for (char l : word) {
            if (result.empty() || l >= result[0]) {
                result = l + result;
            }
            else {
                result += l;
            }
        }

        cout << "Case #" << test << ": " << result << endl;
    }
}
