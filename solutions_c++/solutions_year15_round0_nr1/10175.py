

#include <iostream>
#include <vector>

using namespace std;

int friends_needed(vector<int> s) {
    int stands = 0;
    int friends = 0;
    
    for (int i = 0; i < int(s.size()); i++) {
        if (s[i] == 0)
            continue;
        else if (stands >= i) {
            stands += s[i];
        } else {
            friends += i - stands;
            stands += friends;
            stands += s[i];
        }
    }
    return friends;
}

vector<int> s2v(string &s) {
    vector<int> res;
    for (char c : s)
        res.push_back(c - '0');
    return res;
}

int main(void) {
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++) {
        string smax; cin >> smax;
        string sarr; cin >> sarr;
        cout << "Case #" << t << ": " << friends_needed(s2v(sarr)) << endl;
    }
    
    
return 0;   
}