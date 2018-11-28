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
#include <cmath>
#include <list>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define forn(i, h) forin(i, 0, h)
#define forin(i, l, h) for(ll i = l; i < h; i++)
#define INF 987654321
void solve(istream & in, ostream & out);
void solveAll(istream & in, ostream & out);
string toStr(ll n);

ll revBit(ll bits) {
    ll res = 0;
    while(bits > 0) {
        res <<= 1;
        res |= (bits & 1);
        bits >>= 1;
    }
    return res;
}

ll toBase(ll inter, ll base) {
    ll res = 0;
    inter = revBit(inter);
    while(inter > 0) {
        res *= base;
        res += (inter & 1);
        inter >>= 1;
    }
    return res;
}

string bin(ll num) {
    string res;
    while (num > 0) {
        res.push_back((num & 1) + '0');
        num >>= 1;
    }
    reverse(res.begin(), res.end());
    return res;
}

ll divisor(ll num) {
    ll lim = sqrt(num) + 2;
    forin(i, 3, lim) {
        if (num % i == 0) {
            return i;
        }
    }
    return -1;
}

string parsed(ll n, ll j) {
    stringstream ss;
    ss << "\n";
    ll first = 1;
    forn(i, n - 1) {
        first <<= 1;
    }
    first |= 1;

    ll done = 0;
    list<pair<ll, vector<ll>>> result;
    for(ll num = first; done < j; num += 2) {
        vector<ll> divs;
        divs.reserve(10);
        bool inval = false;
        forin(i, 2, 11) {
            ll d = divisor(toBase(num, i));
            if(d == -1) {
                inval = true;
                break;
            }
            else {
                divs.push_back(d);
            }
        }
        if (!inval) {
            done++;
            result.push_back(pair<ll, vector<ll>>(num, divs));
        }
    }

    for(auto res : result) {
        ss << bin(res.first) << " ";
        forn(i, 8) {
            ss << res.second[i] << " ";
        }
        ss << res.second[8] << "\n";
    }

    return ss.str();
}

void solve(istream & in, ostream & out) {
    ll n, j;
    in >> n >> j;
    out << parsed(n, j);
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
