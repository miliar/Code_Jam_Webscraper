#include <iostream>
#include <string>

using namespace std;

unsigned int flips(string& stack) {
    unsigned int count = (stack.back() == '-') ? 1 : 0;
    char curr = stack[0];
    for (auto it = stack.begin()+1; it != stack.end(); ++it) {
        if (curr != *it) {
            count++;
            curr = *it;
        }
    }
    return count;
}

int main(int argc, char * argv[]) {
    int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        string stack; 
        cin >> stack;
        cout << "Case #" << i << ": " << flips(stack) << endl;    
    }

    return 0;
}
