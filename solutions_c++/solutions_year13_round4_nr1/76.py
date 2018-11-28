#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cassert>

const char* input_file = "A-large.in";
const int Mod = 1000002013;

using namespace std;

struct Node {
    int type; // 0 for enter 1 for leave
    int pos;
    int count;

    Node(int t, int p, int c) : type(t), pos(p), count(c) {}

    bool operator <( const Node& n) const {
        return pos < n.pos || pos == n.pos && type < n.type;
    }
};

vector<Node> nodes;

struct Card {
    int pos;
    int count;

    Card(int p, int c) : pos(p), count(c) {}
};

vector<Card> cards;

int N, M;
long long calc_money(int start_pos, int end_pos) {
    long long first = N;
    long long last = N + start_pos - end_pos;
    long long item = (end_pos - start_pos + 1);
    return (first + last) * item / 2 % Mod;
}

void solve() {
    cin >> N >> M;

    long long ans = 0;
    nodes.clear();
    for (int i =0 ; i < M; ++i) {
        int s, e, p;
        cin >> s >> e >> p;
        nodes.push_back(Node(0, s, p));
        nodes.push_back(Node(1, e, p));

        ans += calc_money(s, e) * p;
        ans %= Mod;
    }


    sort(nodes.begin(), nodes.end());

    //cout <<N << " "<< M << " "<< nodes.size();

    cards.clear();

    for (auto& node : nodes) {
        if (node.type == 0) {
            cards.push_back(Card(node.pos, node.count));
        } else {
            int need = node.count;
            while (need > 0) {
                assert(cards.size() > 0);
                auto f = cards.size() - 1;
                int cnt = min(need, cards[f].count);
                ans -= calc_money(cards[f].pos, node.pos) * cnt;
                ans %= Mod;
                cards[f].count -= cnt;
                need -= cnt;
                if (cards[f].count == 0) cards.pop_back();
            }
        }
    }

    assert(cards.size() == 0);

    ans = (ans + Mod) % Mod;
    cout << ans;
}

int main() {
    freopen(input_file, "r", stdin);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

