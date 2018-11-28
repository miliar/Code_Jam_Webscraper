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
#include <list>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define forn(i, h) forin(i, 0, h)
#define forin(i, l, h) for(ll i = l; i < h; i++)
#define INF 987654321
void solve(istream & in, ostream & out);
void solveAll(istream & in, ostream & out);

int comp(const list<char> & a, const list<char> & b) {
    auto ita = a.begin();
    auto itb = b.begin();
    while(true) {
        if (ita == a.end()) {
            if (itb == b.end()) { return 0; }
            return -*itb;
        }
        else if (itb == b.end()) {
            return *ita;
        }
        if (*ita != *itb) {
            return *ita - *itb;
        }
        ita++;
        itb++;
    }
}

string parsed(const string & in) {
    list<char> res;
    res.push_back(in[0]);

    forin(i, 1, in.size()) {
        char toPut = in[i];
        list<char> l = res;
        l.push_front(toPut);
        list<char> r = res;
        r.push_back(toPut);
        if (comp(l, r) > 0) {
            res.push_front(toPut);
        }
        else {
            res.push_back(toPut);
        }
    }

    stringstream ss;
    for(char c : res) {
        ss << c;
    }
    return ss.str();
}

void solve(istream & in, ostream & out) {
    string s;
    in >> s;
    out << parsed(s);
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
