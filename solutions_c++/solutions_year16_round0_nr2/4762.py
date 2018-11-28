#include <iostream>

using namespace std;

int main()
{
    int numCases;
    string stack;

    cin >> numCases;

    for (int i = 0; i < numCases; ++i) {
        int flips = 0;
        string stack;
        cin >> stack;

        string expectedStack(stack.size(), '+');

        while (stack != expectedStack) {
            for (int j = 0; j < stack.size(); ++j) {
                if (stack[j] == '\0')
                    break;
                else if (stack[j] == stack[j + 1]) {
                    continue;
                }
                else {
                    // This differs from the previous flick them
                    // 0..j-1
                    string replacement(j + 1, (stack[j] == '+' ? '-' : '+'));
                    stack.replace(0, j+1, replacement);
                    flips++;

                    if (stack == expectedStack) {
                        break;
                    }
                }
            }
        }

        cout << "Case #" << i + 1 << ": " << flips << endl;
    }
}

