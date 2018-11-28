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

ll exp(ll base, ll pow) {
    if (pow == 0) { return 1; }
    ll hp = exp(base, pow / 2);
    hp *= hp;
    if (pow & 1) { hp *= base; }
    return hp;
}



string parsed(ll k, ll c, ll s) {
    ll sizeOfLast = exp(k, c - 1);
    stringstream ss;
    forn(i, k) {
        ss << (i * sizeOfLast + 1) << " ";
    }
    return ss.str();
}

void solve(istream & in, ostream & out) {
    ll k, c, s;
    in >> k >> c >> s;
    out << parsed(k, c, s);
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
