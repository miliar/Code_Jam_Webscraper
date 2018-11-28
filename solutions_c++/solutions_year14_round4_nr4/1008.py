#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

typedef long long lld;

struct Trie {
    typedef vector< Trie* > Next;
    Next next;
    int count;
    bool isEnd;

    Trie(): next(getIndex('Z') + 1),
    count(0), isEnd(false) {}

    bool add(const string &s, int start = 0);
    int nodes() const;

    ~Trie() {
        for (auto e : next) {
            if (e) {
                delete e;
            }
        }
    }

private:

    static char getIndex(const char &c) {
        return c - 'A';
    }

    char getChar(const Next::iterator &i) {
        return 'A' + (i - next.begin());
    }

    static char getChar(const int &i) {
        return 'A' + i;
    }
};

bool Trie::add(const string &s, int start) {
    if (start == s.size()) {
        if (isEnd) {
            return false;
        }
        isEnd = true;
        count++;
        return true;
    }
    bool result = false;
    Trie* &e = next[s[start] - 'A'];
    if (e == NULL) {
        e = new Trie();
        result = true;
    }
    result = e->add(s, start + 1) || result;
    if (result) {
        count++;
    }
    return result;
}

int Trie::nodes() const {
    int res;
    if (isEnd) {
        res = 1;
    }
    else {
        res = 0;
        for (auto e : next) {
            if (e != NULL) {
                res = 1;
                break;
            }
        }
        if (res == 0) {
            return 0;
        }
    }
    for (auto e : next) {
        if (e != NULL) {
            res += e->nodes();
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cout << "Case #" << ti << ": ";
        int n, m;
        cin >> m >> n;
        vector< string > ss(m);
        for (auto &s : ss) {
            cin >> s;
        }
        int worst_nodes = -1;
        int worst_count;
        for (vector< int > t(m);; t[0] += 1) {
            bool finished = false;
            for (int i = 0; i < m; ++i) {
                if (t[i] == n) {
                    t[i] = 0;
                    if (i + 1 != m) {
                        t[i + 1] += 1;
                    }
                    else {
                        finished = true;
                    }
                }
            }
            if (finished) {
                break;
            }
            // for (int i = 0; i < m; ++i) { cout << t[i] << " "; }
            vector< Trie > tries(n);
            for (int i = 0; i < m; ++i) {
                tries[t[i]].add(ss[i]);
            }
            int cur_nodes = 0;
            for (int i = 0; i < n; ++i) {
                cur_nodes += tries[i].nodes();
            }
            if (cur_nodes > worst_nodes) {
                worst_nodes = cur_nodes;
                worst_count = 1;
            }
            else if (cur_nodes == worst_nodes) {
                worst_count += 1;
            }
        }
        cout << worst_nodes << " " << worst_count << "\n";
    }
    return 0;
}
