#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define vs vector<string>
#define sz(v) (int)v.size()

int n, m;
string s[10];
vs server[10];
int c = 0;
int ans, ways;
struct Trie {
    Trie *next[26];
    Trie() {
        for(int i =0 ; i < 26 ; i++) {
            next[i] = NULL;
        }
        c++;
    }
    ~Trie() {
        for(int i = 0 ; i < 26 ; i++) {
            delete next[i];
        }
    }
    void add(string s) {
        if( sz(s) == 0 ) {
            return;
        }
        if( next[s[0] - 'A'] == NULL ) {
            next[s[0] - 'A'] = new Trie();
        }
        next[s[0] - 'A'] -> add(s.substr(1));
    }
};

int MakeTrie(vs& store) {
    c = 0;
    Trie *temp = new Trie();
    for(int i = 0 ; i < sz(store) ; i++) {
        temp -> add(store[i]);
    }
    delete temp;
    return c;
}

void comb(int cur) {
    if( cur == m ) {
        int tans = 0;
        for(int i = 0 ; i < n ; i++) {
            if( sz(server[i]) == 0 ) {
                return;
            }
            tans += MakeTrie(server[i]);
        }

        if( tans > ans ) {
            ans = tans;
            ways = 1;
        } else if( ans == tans ) {
            ways++;
        }
        return;
    }
    for(int i = 0 ; i < n ; i++) {
        server[i].push_back(s[cur]);
        comb(cur + 1);
        server[i].pop_back();
    }
}
int main() {
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        cin >> m >> n;
        for(int i = 0 ; i < m ; i++) {
            cin >> s[i];
        }
        ans = 0;
        comb(0);
        printf("Case #%d: %d %d\n", t, ans, ways);
    }
}