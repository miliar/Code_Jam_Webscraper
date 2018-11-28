#include <iostream>
#include <string>

using namespace std;

int main() {

    int cases;
    cin >> cases;
    for (int casei = 0; casei < cases; casei++) {

        int flips = 0;
        string stack;
        cin >> stack;
        stack += "+";
        char last = stack[0];

        for (int i = 1; i < stack.size(); i++) {
            if (stack[i] != last) {
                flips++;
                last = stack[i];
            }
        }

        cout << "Case #" << casei+1 << ": " << flips << endl;
    }

}
