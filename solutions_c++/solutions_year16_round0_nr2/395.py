#include <iostream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

inline char flip(char& c) {
    return (c == '+' ? '-' : '+');
}

int flips = 0;
void flip_stack(string& pancakes, int n) {
    queue<char> tmp;
    for(int i = 0; i < n; ++i) {
        tmp.push(flip(pancakes.back()));
        pancakes.pop_back();
    }
    for(int i = 0; i < n; ++i) {
        pancakes.push_back(tmp.front());
        tmp.pop();
    }
    flips++;
}

void solve(string& pancakes) {

    flips = 0;

    int b = 0;
    while(b < pancakes.size() && pancakes[b] == '+')
        b++;

    while(b < pancakes.size()) {
        //cout << pancakes << endl;

        if(pancakes.back() == '+') {
            flip_stack(pancakes, pancakes.size() - pancakes.find_last_of('-') - 1);
        }
        flip_stack(pancakes, pancakes.size() - b);

        while(b < pancakes.size() && pancakes[b] == '+')
        b++;
    }

    cout << flips << endl;
}

int main() {
    int T;
    cin >> T;
    int c = 1;
    while(T --> 0) {
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        cout << "Case #" << c++ << ": ";
        solve(s);
    }
}