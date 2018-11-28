#include <iostream>
#include <string>

using namespace std;

void flip(string& stack, int start) {
    for (int i = 0; 2*i < start; i++) {
        char tmp = stack[i];
        stack[i] = stack[start-i];
        stack[start-i] = tmp;

        if (stack[i] == '+') {
            stack[i] = '-';
        } else {
            stack[i] = '+';
        }

        if (stack[start-i] == '+') {
            stack[start-i] = '-';
        } else {
            stack[start-i] = '+';
        }
    }

    if (start % 2 == 0) {
        if (stack[start/2] == '+') {
            stack[start/2] = '-';
        } else {
            stack[start/2] = '+';
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string stack;
        cin >> stack;

        int movements = 0;
        for (int i = stack.length()-1; i >= 0; i--) {
            if (stack[i] == '+') {
                continue;
            }

            if (stack[0] == '-') {
                movements++;
                flip(stack, i);
            } else {
                int j = 0;
                while (stack[j+1] == '+') {
                    j++;
                }
                movements++;
                flip(stack, j);

                movements++;
                flip(stack, i);
            }
        }

        std::cout << "Case #" << t << ": " << movements << endl;
    }
}