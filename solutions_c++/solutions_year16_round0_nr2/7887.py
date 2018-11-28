#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; t++) {
        string stack;
        cin >> stack;
        int flips = 0;
        int toflip, finished, L = stack.size();
        do {
            // Count pancakes at the bottom already on the right side
            finished = 0;
            while (finished < L && stack.at(L-1-finished) == '+')
                finished++;
            if (L == finished)
                break;
            // Count pancakes on the top that we will flip
            toflip = 0;
            while (toflip < (L-finished) && stack.at(toflip) == '+')
                toflip++;
            // Flip the top
            if (toflip != 0)
                flips++;
            // Flip the whole stack minus the finished part
            flips++;
            // Restart with the rest
            stack = stack.substr(toflip, L-finished-toflip);
            // Only compute the actual flip on the rest
            L = stack.size();
            for(int i=0; i<L/2; i++) {
                char tmp = stack[i];
                stack[i] = ((stack[L-1-i] == '+') ? '-' : '+');
                stack[L-1-i] = ((tmp == '+') ? '-' : '+');
            }
            if ((L%2) == 1)
                stack[L/2] = ((stack[L/2] == '+') ? '-' : '+');
        } while (L > 0);
        cout << "Case #" << t << ": " << flips << "\n";
    }
}
