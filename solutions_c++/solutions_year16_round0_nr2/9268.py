#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;


int solve(string str) {
    vector<char> stack;

    for (int i = 0; i < (int)str.size(); ++i) {
        if (stack.empty() || stack.back() != str[i]) {
            stack.push_back(str[i]);
        }
    }

    int count = 0;
    int right = (int)stack.size() - 1;
    while (right > 0) {
        if (stack[right] == '-') {
            ++count;
            if (stack[0] == '+') {
                reverse(stack.begin(), stack.begin() + right);
                for (int i = 0; i < right; ++i) {
                    stack[i] = (stack[i] == '-') ? '+' : '-';
                }
            } else {
                reverse(stack.begin(), stack.begin() + right + 1);
                for (int i = 0; i < right; ++i) {
                    stack[i] = (stack[i] == '-') ? '+' : '-';
                }
            }
        }
        --right;
    }
    if (stack[0] == '-') {
        count ++;
    }
    return count;
}


int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        string str;
        cin >> str;
        cout << "Case #" << i << ": " << solve(str) << endl;
    }
    return 0;
}
