#include <iostream>
#include <string>

using namespace std;
int main(int argc, char** argv)
{
    int T, N;
    int count;
    string stack;
    char curr, prev;
    cin >> T;
    cin.get();
    for (int i = 1; i <= T; ++i) {
        count = 0;
        getline(cin, stack);
        if (stack[0] == '-') count++;
        for (int j = 1; j < stack.size(); ++j) {
            if (stack[j] != stack[j-1] && stack[j-1] == '+')
                count += 2;
        }
        cout << "Case #" << i << ": " << count << endl;
    }
}
