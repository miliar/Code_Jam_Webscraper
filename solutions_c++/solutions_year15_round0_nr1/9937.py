#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int T_MIN = 0;
const int T_MAX = 100;
const int S_MIN = 0;

///* Small
const int S_MAX = 6;
//*/

/* Large
const int S_MAX = 1000;
*/

void ovation(int test);

int main() {
    int tests;
    cin >> tests;

    for (int i = 0; i < tests; ++i) ovation(i);
}

void ovation(int test) {
    int s_max;
    string levels;

    cin >> s_max >> levels;
    ++s_max;

    int s[S_MAX];

    for (int k = 0; k < s_max; ++k) {
        char letter = levels[k];
        s[k] = atoi(&letter);
    }

    int count = 0;
    int min = 0;
    for (int i = 0; i < s_max; ++i) {
        if (count < i) {
            min += i - count;
            count += i - count;
        }

        count += s[i];
    }

    cout << "Case #" << test + 1 << ": " << min << endl;
}
