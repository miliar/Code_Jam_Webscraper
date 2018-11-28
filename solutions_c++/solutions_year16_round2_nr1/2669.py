#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <set>
#include <map>
#include <fstream>

typedef int I;
typedef long L;
typedef long long LL;

using namespace std;
typedef vector<I> vi;
typedef vector<vector<I> > vvi;
typedef vector<pair<I,I> > vii;
typedef vector<LL> vL;


#define debug(x) cout << #x << " : " << x << endl

#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = n; n >= 0; --i)
#define all(v) v.begin(),v.end()

int binpow (int a, int n) {
    int res = 1;
    while (n) {
        if (n & 1)
            res *= a;
        a *= a;
        n >>= 1;
    }
    return res;
}

bool removeSymbol(string& s, char c) {
    auto it = find(s.begin(), s.end(), c);
    if (it == s.end())
        return false;
    s.erase(it);
    return true;
}

template<typename Iter>
void req(Iter it, Iter e, string& s, vi& collection) {
    if (it == e) {
        return;
    }
    bool f = true;
    string sc;
    while (true) {
        sc = s;
        for (const auto& c: it->first) {
            f &= removeSymbol(s,c);
        }
        if (f) {
            collection.push_back(it->second);
        } else {
            break;
        }
    }
    req(++it, e, sc, collection);
}

int main()
{
    ifstream in("A-large.in");

    ofstream out("A-large.out");

    map<int, string> ds;
    std::vector<pair<string, int>> sd {{"ZERO", 0},
                         {"TWO", 2},
                         {"SIX", 6},
                         {"EIGHT", 8},
                         {"SEVEN", 7},
                         {"FIVE", 5},
                         {"THREE", 3},
                         {"NINE", 9},
                         {"ONE", 1},
                         {"FOUR", 4}};



    int t;
    in >> t;

    rep(z,t) {
        string s;
        in >> s;
        vi res;
        req(all(sd), s, res);
        std::sort(all(res));
        out << "Case #" << z+1 << ": " ;
        copy(all(res), ostream_iterator<int>(out, ""));
        out << endl;
    }

    return 0;
}

