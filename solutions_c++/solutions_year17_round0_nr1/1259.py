#include <sys/types.h>
#include <unistd.h>
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define RFOR(i, a, b) for (int i = (b)-1; i >= int(a); --i)
#define rep(i, n) FOR(i, 0, n)
#define rep1(i, n) FOR(i, 1, int(n) + 1)
#define rrep(i, n) RFOR(i, 0, n)
#define rrep1(i, n) RFOR(i, 1, int(n) + 1)
#define all(c) begin(c), end(c)
const int MOD = 1000000007;

template <typename T>
void __dump__(std::ostream &os, const T &first) {
    os << first;
}
template <typename First, typename... Rest>
void __dump__(std::ostream &os, const First &first, const Rest &... rest) {
    os << first << ", ";
    __dump__(os, rest...);
}
#define dump(...)                                         \
    do {                                                  \
        std::ostringstream os;                            \
        os << __LINE__ << ":\t" << #__VA_ARGS__ << " = "; \
        __dump__(os, __VA_ARGS__);                        \
        std::cerr << os.str() << std::endl;               \
    } while (0)

string solve(const string &s) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    int ans = 0;
    rep(i, 100000000) ans ^= i;
    dump(s);
    return s + s + to_string(ans);
}

vector<tuple<string, int>> input;
vector<string> output;

string solve(string s, int k) {
    char flip = '+' ^ '-';
    int n = s.size();
    int ans = 0;
    rep(i, n - k + 1) {
        if (s[i] == '-') {
            ++ans;
            rep(j, k) {
                s[i + j] ^= flip;
            }
        }
    }
    rep(i, n) if (s[i] == '-') return "IMPOSSIBLE";
    return to_string(ans);
}

mutex mtx;
queue<int> q;

void worker() {
    while (1) {
        int id;
        {
            lock_guard<mutex> lock(mtx);
            if (q.empty()) break;
            id = q.front();
            q.pop();
        }
        output[id] = solve(get<0>(input[id]), get<1>(input[id]));
    }
}

int main() {
    const int NUM_THREAD = 7;
    int T;
    cin >> T;
    input.resize(T);
    output.resize(T);
    rep(i, T) {
        string s;
        int k;
        cin >> s >> k;
        input[i] = make_tuple(s, k);
    }

    rep(i, T) q.push(i);
    vector<thread> ths(NUM_THREAD);
    for (auto &th : ths) th = thread(worker);
    for (auto &th : ths) th.join();

    rep(i, T) {
        printf("Case #%d: %s\n", i + 1, output[i].c_str());
    }
}
