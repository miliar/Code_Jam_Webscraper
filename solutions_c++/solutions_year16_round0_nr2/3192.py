/* Author: Ankit Sultana
 * * * * * * * * * * * */
#include <iostream>
#include <cassert>
#define MAXN 103

using namespace std;

void flip(string &x, int size) {
    reverse(x.begin(), x.begin() + size);
    for(int i = 0; i < size; i++) x[i] = x[i] == '+'?'-': '+';
}
int leading(string &x) {
    int size = 0;
    if(x[0] == '-') return 0;
    while(size < x.size()) {
        if(x[size] == '-') {
            flip(x, size);
            return 1;
        }
        size++;
    }
    assert(false);
    return 0;
}

int last_index(string &x) {
    for(int i = x.size()-1; i >= 0; i--) {
        if(x[i] == '-') return i;
    }
    return -1;
}

int main() {
    int t;
    cin >> t;
    for(int tc = 1; tc <= t; tc++) {
        string input;
        cin >> input;
        int answer = 0;
        while(true) {
            int idx;
            if((idx = last_index(input)) != -1) {
                answer += leading(input);
                flip(input, idx+1);
            } else {
                break;
            }
            answer++;
        }
        cout << "Case #" << tc << ": " << answer << '\n';
    }
    return 0;
}
