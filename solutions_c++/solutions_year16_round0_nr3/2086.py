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

vector<int> primes;

void getPrimes() {
    int last = 70000;
    primes.reserve(10000);

    for (int i = 2; i < last; ++i) {
        bool prime = true;
        for (int x: primes) 
            if (i % x == 0) {
                prime = false; 
                break;
            }
        if (prime) primes.push_back(i);
    }
}

int getDivisor(long long x) {
    int st = sqrt(x) + 1;
    for (int y: primes) {
        if (y > st) break;
        if (x % y == 0)
            return y;
    }

    return -1;
}

void next_p(string& s) {
    int i = int(s.size()) - 2;
    for (; s[i] == '1' && i >= 0; s[i] = '0', --i);
    assert(i > 0);
    s[i] = '1';
}

int main() { 
    getPrimes();
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

    int t, n, j;
    cin >> t;
    for (int o = 0; o < t; ++o) {
        cin >> n >> j;
        cout << "Case #" << o + 1 << ":\n";
        string s(n, '0');
        s[0] = s.back() = '1';

        vector<int> res;
        for (int i = 0; i < j;) {
            res.clear();
            for (int k = 2; k < 11; ++k) {
                long long v = stoll(s, NULL, k);
                res.push_back(getDivisor(v));
                if (res.back() == -1) {
                    res.pop_back();
                    break;
                }
            }
            if (res.size() == 9) {
                cout << s << " ";
                for (int x: res)
                    cout << x << " ";
                cout << "\n";
                i++;
                cerr << i << endl;
            }

            next_p(s);
        }
    }

    return 0;
}
