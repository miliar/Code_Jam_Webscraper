#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getMinFriends(const vector<int>& shyness) {
    int current = shyness[0];
    int needed = 0;
    int smax = shyness.size() - 1;
    for (int s = 1; s <= smax; s++) {
        if (s > current + needed) {
            needed = s-current;
        } 
        current += shyness[s];
    }
    return needed;
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        char c;
        int smax;
        vector<int> shyness;
        
        cin >> smax;
        for (int i = 0; i <= smax; i++) {
            cin >> c;
            shyness.push_back((int) (c-'0'));
        } 
   
        cout << "Case #" << t << ": " << getMinFriends(shyness) << '\n';
        /*
        for (auto s : shyness) {
            cout << s;
        }
        cout << '\n';
        */
    }

    return 0;
}
