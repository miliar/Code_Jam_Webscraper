#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int a = 1; a<=t; a++) {
        string s;
        vector<int> translate;
        cin >> s;
        for(auto c : s)
            translate.push_back(c == '+' ? 1 : 0);
        int flips = 0;
        for(auto it = translate.rbegin(); it != translate.rend(); it++)
            if(!((*it + flips) % 2)) flips ++;

        cout << "Case #" << a << ": " << flips << endl;
    }
    return 0;
}