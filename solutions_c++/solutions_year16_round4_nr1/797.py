#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;
int T, R, P, S, N;

string k[20000];

string gen(string x) {
    string l;
    for(int i = 0; i < x.size(); i++) {
        l = l + k[x[i]];
    }
    return l;
}

string iterate(string x) {
    for(int i = 0; i < N; i++) {
        x = gen(x);
    }
    return x;
}

bool matches(string k) {
    //cerr << "Testing " << k << "\n";
    int r = 0;
    int s = 0;
    int p = 0;
    for(int i = 0; i < k.size(); i++) {
        char j = k[i];
        if(k[i] == 'R') {
            r++;
        }
        if(k[i] == 'S') {
            s++;
        }
        if(k[i] == 'P') {
            p++;
        }
    }
    return r == R && s == S && p == P;
}

string test() {
   string s;
   s = iterate("R");
   if(matches(s)) {
        return s;
   }
   s = iterate("P");
   if(matches(s)) {
        return s;
   }
   s = iterate("S");
   if(matches(s)) {
        return s;
   }
   return "";
}

string lexo(string s) {
    if (s.size() == 1) {
        return s;
    } else {
        string s1 = s.substr(0, s.size()/2);
        string s2 = s.substr(s.size()/2, s.size()/2);
        s1 = lexo(s1);
        s2 = lexo(s2);
        vector<string> v;
        v.push_back(s1);
        v.push_back(s2);
        sort(v.begin(), v.end());
        return v[0] + v[1];
    }
}

int main() {
    k['R'] = "RS";
    k['S'] = "SP";
    k['P'] = "PR";
    cin >> T;
    for(int t = 1; t <= T; t++) {
        //cerr <<"CASE " << t << "--\n";
        cin >> N >> R >> P >> S;
        string s = test();
        if (s == "") {
            cout << "Case " << "#" << t << ": ";
            cout << "IMPOSSIBLE\n";
        } else {
            //cerr <<"AMHERE\n";
            s = lexo(s);
            cout << "Case " << "#" << t << ": ";
            cout << s << "\n";
        }
    }
    return 0;
}
