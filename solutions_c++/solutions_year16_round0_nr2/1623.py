#include <iostream>
#include <map>

using namespace std;

long long t;
string s;
map<string, int> m, m2;

string flip(string t, int k) {
    string neo = t;

    for (int i = 1; i <= k;i++)
        neo[i-1] = (t[k-i] == '+' ? '-' : '+');

    return neo;
}

void rec(string t, int steps) {
    if (m.count(t) > 0 && m[t] <= steps)
        return;
    if (!m.count(t))
        m.insert(pair<string,int>(t, steps)); 
    else 
        m[t] = steps;    
    int n = t.length();

    for (int i = 1; i <= n; i++)
        rec(flip(t, i), steps+1);
}


void init() {
    string t;
    for (int i = 0; i < 10; i++) {
        t += '+';
        //cout << t << endl;
        //m.insert(pair<string,int>(t, 0));
        rec(t, 0);
    }
}

long long calc(string s) {
    return m[s];   
}

int calc2(string s) {
    s += '+';
    
    int res = 0;
    for (int i = 0; i < s.length()-1; i++) {
        res += (s[i] != s[i+1]);
    }
    return res;
}

int main() {
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cin >> s;
        int res = calc2(s);
        cout << "Case #"<< i<<": ";
        cout << res << endl;
    }
    return 0;
}   
