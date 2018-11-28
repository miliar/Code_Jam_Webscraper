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

void solve(int x) {
    static bool used[10];
    memset(used, false, sizeof(used));

    int cnt = 0;
    int cur_x = 0;
    for (int i = 0; i < 1000 && cnt < 10; ++i) {
        if (cur_x > numeric_limits<int>::max() - x)
            break;
        for (int temp = cur_x += x; temp > 0; temp /= 10) {
            int a = temp % 10;
            cnt += !used[a];
            used[a] = true;
        }
    }

    if (cnt == 10)
        cout << cur_x << "\n";
    else
        cout << "INSOMNIA\n";
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

    int n;
    cin >> n;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        cout << "Case #" << i + 1 << ": ";
        solve(x);
    }
    
    return 0;
}
