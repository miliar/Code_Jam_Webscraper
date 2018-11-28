#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main() {
    freopen("RevengeOfThePanCakes.in", "rt", stdin);
    freopen("RevengeOfThePanCakes.out", "wt", stdout);
    
    int numTests;
    string line;
    getline(cin, line);
    istringstream iss(line);
    iss >> numTests;
    
    for (int i = 0; i < numTests; ++i) {
        string stack;
        getline(cin, stack);

        int size = (int) stack.size();
        
        int cnt = 1;
        for (int i = 0; i < size - 1; ++i) {
            if (stack[i] != stack[i + 1]) {
                ++cnt;
            }
        }

        if (stack[size - 1] == '+') {
            --cnt;
        }
        
        cout << "Case #" << i + 1 << ": " << cnt<< endl;
    }
    
    return 0;
}
