#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

struct TView {
    const std::string* data;
    int begin;
    int end;
    int rev;
    int flip;

    TView(const std::string* s) 
        : data(s) 
        , begin(0)
        , end(s->size() - 1)
        , rev(false)
        , flip(false)
    {
    }

    bool back() const {
        bool ans;

        if (rev) {
            ans = (*data)[begin] == '+';
        } else {
            ans = (*data)[end] == '+';
        }

        if (flip) ans ^= true;

        return ans;
    }

    bool front() const {
        bool ans;

        if (rev) {
            ans = (*data)[end] == '+';
        } else {
            ans = (*data)[begin] == '+';
        }

        if (flip) ans ^= true;

        return ans;
    }

    TView pop() const {
        TView ans = *this;
        if (ans.rev) {
            ++ans.begin;
        } else {
            --ans.end;
        }
        return ans;
    }

    bool empty() const {
        return begin > end;
    }

    TView turn() const {
        TView ans = *this;
        ans.rev ^= true;
        ans.flip ^= true;
        return ans;
    }
};

const int N = 101;
int CACHE[N][N][2][2][2];

int solve(TView s, bool target) {
    if (s.empty()) {
        return 0;
    }

    if (s.back() == target) {
        return solve(s.pop(), target);
    }

    int& ans = CACHE[s.begin][s.end][s.flip][s.rev][target];
    if (ans != -1) {
        return ans;
    }
    ans = 1e9;

    if (s.front() != target) {
        TView s2 = s.turn();
        ans = min(ans, 1 + solve(s2, target));        
    } else {
        TView s2 = s.turn();
        ans = min(ans, 1 + solve(s2.pop(), !target) + 1);
    }
    ans = min(ans, solve(s.pop(), !target) + 1);

    return ans;
}

int main() {
    #ifdef LOCAL
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif    	   	

    int T;
    cin >> T;
    for (int __it = 1; __it <= T; ++__it) {
        string s;
        cin >> s;

        memset(CACHE, -1, sizeof(CACHE));

        TView view(&s);
        int ans = solve(view, true);

    	cout << "Case #" << __it << ": " << ans << endl;
    }

    return 0;
}
