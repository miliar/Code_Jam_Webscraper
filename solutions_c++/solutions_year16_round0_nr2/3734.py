#include <iostream>
#include <queue>
#include <set>
#include <utility>

using namespace std;

bool check(string s, int len) {
    for(int i=0; i<len; i++) {
        if(s[i] != '+') return false;
    }
    return true;
}

string flip(string s) {
    int len = s.length();
    int half = len/2;

    for(int i=0; i<half; i++) {
        char first = s[i] == '+' ? '-' : '+';
        char second = s[len-i-1] == '+' ? '-' : '+';
        s[len-i-1] = first;
        s[i] = second;
    }

    if(len%2 == 1) {
        s[half] = s[half] == '+' ? '-' : '+';
    }

    return s;
}

int main() {
    // string f; cin >> f;  int l = f.length();
    // for(int j=1; j<=l; j++) { cout << flip(f.substr(0,j)) << endl; }
    int T, len;
    string s;
    cin >> T;
    for(int i=0; i<T; i++) {
        cin >> s;
        len = s.length();
        queue<pair<string, int>> fringe;
        set<string> visited;
        fringe.push(make_pair(s, 0));
        
        while(!fringe.empty()) {
            pair<string, int> top = fringe.front();
            visited.insert(top.first);
            fringe.pop();

            if(check(top.first, len)) {
                cout << "Case #" << (i+1) << ": " << top.second << endl;
                break;
            }

            for(int j=len; j>0; j--) {
                string s2 = flip(top.first.substr(0,j)) + top.first.substr(j,len);
                if(visited.find(s2) == visited.end()) {
                    fringe.push(make_pair(s2, top.second+1));
                }
            }
        }
    }
    return 0;
}
