#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string tournament(string start, int d) {
    if(d == 0)
        return start;
    
    string next = "";
    for(int i = 0; i < start.size(); ++i) {
        if(start[i] == 'P')
            next += "PR";
        else if(start[i] == 'R')
            next += "RS";
        else if(start[i] == 'S')
            next += "PS";
    }
    
    return tournament(next, d-1);
}

bool correct(const string &s, int R, int P, int S) {
    for(int i = 0; i < s.size(); ++i) {
        if(s[i] == 'R') R--;
        if(s[i] == 'P') P--;
        if(s[i] == 'S') S--;
    }
    
    return R == 0 && P == 0 && S == 0;
}

void fix(string& s, int i, int l) {
    if(l == 1)
        return;
    
    fix(s, i, l/2);
    fix(s, i + (l/2), l/2);
    //cout << s.substr(i, l/2) << " " << s.substr(i + (l/2), l/2) << endl;
    if(s.substr(i, l/2) > s.substr(i + (l/2), l/2)) {
        for(int j = i; j < i + l/2; ++j) {
            swap(s[j], s[j + (l/2)]);
        }
    }
}

void solve() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    
    vector<string> sols;
    sols.push_back(tournament("R", N));
    sols.push_back(tournament("P", N));
    sols.push_back(tournament("S", N));
    
    for(int i = 0; i < sols.size(); ++i) {
        fix(sols[i], 0, sols[i].size());
    }
    
    sort(sols.begin(), sols.end());
    for(int i = 0; i < sols.size(); ++i) {
        if(correct(sols[i], R, P, S)) {
            cout << sols[i] << endl;
            return;
        }
    }
    
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
