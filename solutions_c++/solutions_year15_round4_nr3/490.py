#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <bitset>
#include <cassert>

using namespace std;

#define NSENTS 200
#define NWORDS 4000
typedef bitset<NSENTS> S;

vector<int> sents[NSENTS];
vector<int> words[NWORDS];
bitset<NSENTS> known;
bitset<NWORDS> left_;
bitset<NWORDS> right_;

#define SAVE(v) auto v##saved = v
#define RESTORE(v) v = v##saved
int N, M;
int total = 0;
int go(int i = 0) {
    if (i == N) {
        return total;
    }
    SAVE(total);
    int best = 10000000;
    SAVE(left_);
    for (int w: sents[i]) if (!left_.test(w)) {
        if (right_.test(w)) ++total;
        left_.set(w);
    }
    best = min(best, go(i+1));
    RESTORE(left_);
    RESTORE(total);
    SAVE(right_);
    for (int w: sents[i]) if (!right_.test(w)) {
        if (left_.test(w)) ++total;
        right_.set(w);
    }
    best = min(best, go(i+1));
    RESTORE(right_);
    RESTORE(total);
    return best;
}

void tc() {
    for (int i = 0; i < NSENTS; ++i) sents[i].clear();
    for (int i = 0; i < NWORDS; ++i) words[i].clear();
    known.reset();
    left_.reset();
    right_.reset();
    total = 0;
    static int cas = 1;
    cout << "Case #" << cas++ << ": ";
    cin >> N;
    cin.ignore();
    unordered_map<string, int> w;
    int next = 0;
    for (int i = 0; i < N; ++i) {
        string s;
        getline(cin, s);
        istringstream in(s);
        while (in >> s) {
            int x = w.insert(make_pair(s, next)).first->second;
            if (x == next) ++next;
            words[x].push_back(i);
            sents[i].push_back(x);
        }
    }
    known.set(0);
    known.set(1);
    for (int x : sents[0]) left_.set(x);
    for (int x : sents[1]) {
        if (!right_.test(x) && left_.test(x)) ++total;
        right_.set(x);
    }
    M = next;
    cout << go() << endl;
}

int main() {
    int T; cin >> T; while (T--) tc();
}
