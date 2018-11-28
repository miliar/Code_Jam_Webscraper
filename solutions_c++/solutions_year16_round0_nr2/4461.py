#include <iostream>

using namespace std;

int compute(string s) {
    char c = '@';
    int nb_groups = 0;
    for(unsigned i = 0 ; i < s.size() ; i++) {
        if(c != s[i])
            nb_groups ++;
        c = s[i];
    }
    if(s[s.size()-1] == '+')
        nb_groups--;
    return nb_groups;
}

int main() {
    int T;
    string s;
    cin >> T;
    for(int i = 1 ; i <= T ; i++) {
        cin >> s;
        cout << "Case #" << i << ": ";
        cout << compute(s);
        cout << "\n";
    }
    return 0;
}
