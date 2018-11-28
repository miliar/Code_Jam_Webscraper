#include <iostream>
#include <vector>
using namespace std;

enum sym {
    ONE, N, I, J, K, NI, NJ, NK, NONE
};

enum sym table[8][8] = {
    {ONE, N, I, J, K, NI, NJ, NK},
    {N, ONE, NI, NJ, NK, I, J, K},
    {I, NI, N, K, NJ, ONE, NK, J},
    {J, NJ, NK, N, I, K, ONE, NI},
    {K, NK, J, NI, N, NJ, I, ONE},
    {NI, I, ONE, NK, J, N, K, NJ},
    {NJ, J, K, ONE, NI, NK, N, I},
    {NK, K, NJ, I, ONE, J, NI, N}
};

int main() {
    int cases;
    cin >> cases;

    for (int x = 0; x < cases; ++x) {
        int length, times;
        cin >> length >> times;
        vector<sym> input;

        for (int i = 0; i < length; ++i) {
            char c;
            cin >> c;
            switch (c) {
            case 'i':
                input.push_back(I);
                break;
            case 'j':
                input.push_back(J);
                break;
            case 'k':
                input.push_back(K);
                break;        
            }
        }

        enum sym running = ONE;
        enum sym goal = I;
        
        for (int j = 0; j < times; ++j)
            for (int i = 0; i < length; ++i) {
                if (running == goal) {
                    // cout << "Change goal" << endl;
                    if (goal == I) goal = J;
                    else if (goal == J) goal = NONE;
                    running = ONE;
                }
                // cout << input[i] << endl;
                running = table[running][input[i]];
            }

        cout << "Case #" << x + 1 << ": ";
        if (goal == NONE && running == K)
            cout << "YES";
        else
            cout << "NO";
        cout << endl;
    }
}