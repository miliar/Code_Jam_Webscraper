#include <iostream>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[]) {
    int e;
    string pancakes;
    cin >> e;
    getline(cin, pancakes);
    for (int i = 0; i < e; i++) {
        int changes = 0;
        char side;
        const char* cakes;
        getline(cin, pancakes);
        cakes = pancakes.c_str();
        side = cakes[0];
        for (int p = 0; p < pancakes.size(); p++) {
            if (side != cakes[p]) {
                changes++;
                side = cakes[p];
            }
        }
        if (cakes[pancakes.size() - 1] == '-') {
            changes++;
        }

        cout << "Case #" << i + 1 << ": " << changes << endl;
    }

    return 0;
}
