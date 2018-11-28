#include <iostream>
#include <string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    string stack;
    getline(cin, stack);
    for(int i = 1; i <= t; i++) {
        string winning = "";
        getline(cin, stack);
        for(int j = 0; j < stack.length(); j++) {
            if (stack[j] >= winning[0]) {
                winning = stack[j] + winning;
            } else {
                winning = winning + stack[j];
            }
        }
        cout << "Case #" << i << ": " << winning << endl;
    }
    return 0;
}