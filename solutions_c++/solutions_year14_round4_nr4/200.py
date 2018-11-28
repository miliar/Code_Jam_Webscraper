#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
#include <map>

using namespace std;

#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

template <typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template <typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template <typename T> inline int sz(const T& x) { return (int) x.size(); }

const double PI = 2 * acos(0);

struct Node {
    
    map<char, Node*> go;

};

struct Trie {
    Node* root;
    int nodes;

    Trie() {
        root = new Node();
        nodes = 0;
    }

    void add(const string& s) {
        Node* u = root;
        for (char c : s) {
            if (u->go.count(c) == 0) {
                u->go[c] = new Node();
                nodes++;
            }
            u = u->go[c];
        }
    }

};

int ansScore, ansWays;
vector<string> ss;
vector<int> st;
        int nStrings, nServers;

void f(int d) {
    if (d == sz(ss)) {
        vector<Trie> tries(nServers);
        forn (i, nStrings) {
            tries[st[i]].add(ss[i]);
        }
        int sum = 0;
        forn (i, nServers) {
            // debug(tries[i].nodes);
            sum += tries[i].nodes;
            if (tries[i].nodes) sum++;
        }
        if (sum > ansScore) {
            ansScore = sum;
            ansWays = 0;
        }
        if (sum == ansScore) {
            ansWays++;
        }
        return;
    }
    forn (i, nServers) {
        st[d] = i;
        f(d + 1);
    }
}

int main() {
    freopen("D-small-attempt0.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    // freopen("in.txt", "r", stdin);

    int nTests;
    cin >> nTests;

    // nTests = 2;
    forn (iTest, nTests) {

        cin >> nStrings >> nServers;

        ss.resize(nStrings);
        forn (i, nStrings) {
            cin >> ss[i];
        }

        ansScore = 0;
        ansWays = 1;

        st.resize(nStrings);
        f(0);

        cout << "Case #" << iTest + 1 << ": ";
        cout << ansScore << ' ' << ansWays << endl;
    }
    return 0;
}