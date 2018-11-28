#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <deque>
#include <queue>

using namespace std;

typedef vector<int> vi;

struct state {
    int A, r, i;
    state(int aa=0, int rr=0, int ii=0) : A(aa), r(rr), i(ii) {}
};

bool operator<(const state& a, const state& b) {
    return a.r > b.r;
}

ostream& operator<<(ostream& os, const state& st) {
    os << "[A:" << st.A << ", r:" << st.r << ", i:" << st.i << "]";
    return os;
}

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int A, N;
        cin >> A >> N;
        vi ms;
        for (int i=0; i<N; ++i) {
            int s;
            cin >> s;
            ms.push_back(s);
        }
        sort(ms.begin(), ms.end());
        const int z = ms.size();
        priority_queue<state> q;
        q.push(state(A, 0, 0));
        while (!q.empty()) {
            state f = q.top();
            // cout << "f = " << f << endl;
            q.pop();
            if (f.i>=z) {
                cout << "Case #" << cs << ": " << f.r << "\n";
                break;
            }
            if (f.A>ms[f.i]) {
                q.push(state(f.A+ms[f.i], f.r, f.i+1));
                continue;
            }
            q.push(state(2*f.A-1, f.r+1, f.i));
            q.push(state(f.A, f.r+1, f.i+1));
        }
    }
}
