#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> counts(2600, 0);

void calc(string &s) {
    char end = s[0];
    vector<char> left, right;
    for (unsigned i = 1; i < s.size(); i++) {
        if (s[i] >= end) {
            left.push_back(s[i]);
            end = s[i];
        } else {
            right.push_back(s[i]);
        }
    }    
    for (int i = left.size()-1; i >= 0; i--) {
        cout << left[i];
    }
    cout << s[0];
    for (unsigned i = 0; i < right.size(); i++) {
        cout << right[i];
    }
}

int main() {
    int testCases;
    string s; 
    cin >> testCases;

    for (int i = 1; i <= testCases; i++) {
        cin >> s;
        cout << "Case #" << i << ": ";
        calc(s);
        cout << endl;
        for (unsigned k = 0; k < counts.size(); k++) {
            counts[k] = 0;
        }
    }

    return 0;
}
