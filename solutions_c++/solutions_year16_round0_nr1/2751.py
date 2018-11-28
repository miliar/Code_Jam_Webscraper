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
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define forn(i, h) forin(i, 0, h)
#define forin(i, l, h) for(ll i = l; i < h; i++)
#define INF 987654321
void solve(istream & in, ostream & out);
void solveAll(istream & in, ostream & out);

string toStr(ll n) {
    stringstream ss;
    ss << n;
    return ss.str();
}

void addDigs(ll num, set<ll> & digs) {
    if (num == 0) {
        digs.insert(0);
        return;
    }
    while (num > 0) {
        ll dig = num % 10;
        digs.insert(dig);
        num /= 10;
    }
}

string parsed(ll n) {
    ll base = n;
    ll num = base;
    set<ll> digs;
    if (num != 0) {
        while(true) {
            addDigs(num, digs);
            if (digs.size() == 10) {
                return toStr(num);
            }
            num += base;
        }
    }
    return "INSOMNIA";
}

void solve(istream & in, ostream & out) {
    ll base;
    in >> base;
    out << parsed(base);
}


int main() {
    ifstream fin("A-large.in");
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

