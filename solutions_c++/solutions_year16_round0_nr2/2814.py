#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <memory>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define forn(i, h) forin(i, 0, h)
#define forin(i, l, h) for(ll i = l; i < h; i++)
#define INF 987654321
void solve(istream & in, ostream & out);
void solveAll(istream & in, ostream & out);
string toStr(ll n);

char f(char c) {
    if (c == '+') return '-';
    return '+';
}



string flip(string s, ll num) {
    string result;
    result = s;
    forn(i, num) {
        result[i] = f(s[num - i - 1]);
    }
    return result;
}

ll longestPEnd(string s) {
    s.push_back('-');
    ll res = -1;
    ll currLen = 0;
    ll maxLen = 0;
    forn(i, s.length()) {
        if (s[i] == '+') {
            currLen++;
            if (currLen > maxLen) {
                maxLen = currLen;
                res = i;
            }
        }
        else {
            currLen = 0;
        }
    }
    return res;
}

ll lastPIndex(const string & s) {
    ll res = -1;
    forn(i, s.length()) {
        if(s[i] == '+') {
            res = max(res, i);
        }
    }
    return res;
}

string parsed(string conf) {
    ll res = 0;
    while(true) {
        while(conf.size() > 0 &&
              conf.back() == '+') {
            conf.pop_back();
        }
        if (conf.size() == 0) { return toStr(res); }
        ll flipAt;

        if (conf.front() == '-') {
            flipAt = conf.length();
        }
        else {
            flipAt = longestPEnd(conf) + 1;
        }

        res++;
        conf = flip(conf, flipAt);
    }
}

void solve(istream & in, ostream & out) {
    string conf;
    in >> conf;
    out << parsed(conf);
}


int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    solveAll(fin, fout);
    return 0;
}

void solveAll(istream & in, ostream & out) {
    ll t;
    in >> t;
    forin(i, 1, t + 1) {
        out << "Case #" << i << ": ";
        solve(in, out);
        out << "\n";
    }
}
string toStr(ll n) {
    stringstream ss;
    ss << n;
    return ss.str();
}
