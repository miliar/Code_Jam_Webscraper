#include <bits/stdc++.h>

using namespace std;
const string nameFiles = "";

#define err(...) { \
    vector<string> variables = split(#__VA_ARGS__, ','); \
    error(variables.begin(), __VA_ARGS__); \
}

void error(vector<string>::iterator) {}

template<typename T, typename... Args>
void error(vector<string>::iterator cur_var, T a, Args...args) {
    cerr << cur_var->substr((*cur_var)[0] == ' ') << " = " << a << endl;
    error(++cur_var, args...);
}

vector<string> split(string const& str, char c) {
    vector<string> res;
    stringstream ss(str);
    string x;
    while (getline(ss, x, c)) 
        res.emplace_back(x);
    return move(res);
}

string to_str(int x) {
    static char buff[64];
    sprintf(buff, "%d", x);
    return std::string(buff);
}

void solve(const string& s) {
    bool parity = 0;
    int res = 0;

    for (int i = int(s.size()) - 1; i >= 0; --i) {
        for (char c = parity ? '-' : '+'; i >= 0 && s[i] == c; --i);
        if (i < 0) break;

        res++;
        parity ^= 1;
    }

    cout << res << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    #ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #else
    if (!nameFiles.empty()) {
        freopen((nameFiles + ".in").c_str(), "r", stdin);
        freopen((nameFiles + ".out").c_str(), "w", stdout);
    }
    #endif

    int t;
    cin >> t;
    string s;
    getline(cin, s);
    for (int i = 0; i < t; ++i) {
        getline(cin, s);
        cout << "Case #" << i + 1 << ": ";
        solve(s);
    }

    return 0;
}
